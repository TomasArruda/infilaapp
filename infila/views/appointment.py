from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, date
from infila.utils import *
from math import *
from django.utils import timezone
from gcm import GCM

from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, ANotification
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer, ANotificationSerializer

class AppointViewSet(viewsets.ModelViewSet):
	queryset = Appointment.objects.all()
	serializer_class = AppointSerializer

	@detail_route(methods=['get'])
	def check(self, request, pk=None):
		queryset = Appointment.objects.get(id=pk)
		now = timezone.now()
		appointdate = queryset.line.date
		nowday = now.day
		appointday = appointdate.day
		nowmonth = now.month
		appointmonth = appointdate.month
		nowyear = now.year
		appointyear = appointdate.year
		if queryset.check == False:
			if nowday == appointday and nowmonth == appointmonth and nowyear == appointyear:
				queryset.check = True
				ahour = queryset.time.hour
				aminutes = queryset.time.minute
				nhour = now.hour
				nminutes = now.minute
				
				dhour = nhour-ahour
				delt = dhour*60 + (nminutes-aminutes)
				if delt < 0:
					delt = 0
				queryset.delay = delt
				queryset.check = True
				queryset.save()
				
				return json_response({'check': 'True','delayMinutes': delt})
			return json_response({'error': 'today is not the appoitment day'})
		return json_response({'error': 'this appointment has already been checked'})

	@detail_route(methods=['get'])
	def waitingTime(self, request, pk=None):
		queryset = Appointment.objects.get(id=pk)
		now = timezone.now()
		appointdate = queryset.line.date
		nowday = now.day
		appointday = appointdate.day
		nowmonth = now.month
		appointmonth = appointdate.month
		nowyear = now.year
		appointyear = appointdate.year
		if queryset.check == False:
			if nowday == appointday and nowmonth == appointmonth and nowyear == appointyear:
				queryset.check = True
				ahour = queryset.time.hour
				aminutes = queryset.time.minute
				nhour = now.hour
				nminutes = now.minute

				delt = (ahour-nhour)*60 + aminutes-nminutes
				queryset2 = Appointment.objects.filter(line = queryset.line, time__lte=queryset.time, check = True)
				
				if not queryset2.exists():
					delay = 0
				else:
					delay = queryset2.reverse()[0].delay
				delt = delt + delay
				
				if delt < 0:
					dhour = 0
					dminutes =0
				else:
					dhour = delt // 60
					dminutes = delt % 60
				
				return json_response({'hour': dhour , 'minutes': dminutes})
			return json_response({'day': appointday,'month': appointmonth,'year': appointyear, 'hour': queryset.time.hour, 'minutes': queryset.time.minute})       
		return json_response({'error': 'this appointment has already been checked'})

	@detail_route(methods=['get'])
	def clearAppointment (self, request, pk=None):
		queryset = Appointment.objects.get(id=pk)
		clinicID = queryset.line.clinic.id
		queryset2 = Admin.objects.filter(clinic__id = clinicID)
		for e in queryset2:
			notification = ANotification.objects.create(flag='desmarque' ,text=pk, admin= e)
		return json_response({'message': 'waiting answer'})
	
	@detail_route(methods=['get'])
	def askForReplace (self, request, pk=None):
		queryset = Appointment.objects.get(id=pk)
		gcm = GCM("AIzaSyCEimvyhdLB38RIIOTITtZ6JwttrWO07JU")
		data = {'message': 'Horario vago do dia '+str(queryset.line.date)+' as '+str(queryset.time)+' com o '+queryset.line.medic.name+' na clinica '+queryset.line.clinic.name+'.', 'year':str(queryset.line.date.year) ,'month':str(queryset.line.date.month), 'day':str(queryset.line.date.day) , 'time': str(queryset.time),'clinic':str(queryset.line.clinic.id), 'medic':str(queryset.line.medic.id)}
		reg_id = 'APA91bF0k32Tyqlhiy9DxfNO7B-6eKNSilMGtfKaehOQ3XV-suYwdwK-3meSTTlCKxUCc5U2B8eAGv5S9bbnAOLe5ww_eqmVyAm5fqVwYyy_dmZCQRRK9veZkZ22K6-Dsj9WNI2LTFeZ6OcwfsQ3NfSh4WyJ8S2tBQ'
		gcm.plaintext_request(registration_id=reg_id, data=data)
		queryset2 = Appointment.objects.filter(line__id=queryset.line.id, check = False, patient__isnull=False)
		for e in queryset2:
			reg_id = e.patient.gcm_id
			if reg_id is not None and not reg_id == "":
				gcm.plaintext_request(registration_id=reg_id, data=data)
		queryset.delete()
		return json_response({'message': 'deleted succefully'})

	@list_route(methods=['get'])
	def showInterest (self, request, pk=None):
		time = request.GET.get('time', '')
		year = request.GET.get('year', '')
		month = request.GET.get('month', '')
		day = request.GET.get('day', '')
		medic = request.GET.get('medic', '')
		clinic = request.GET.get('clinic', '')
		patientID = request.GET.get('patientID', '')
		#now = date.today()
		queryset = Line.objects.get(date__year = year, date__month = month, date__day = day, medic__id= medic, clinic__id=clinic)
		clinicID = queryset.clinic.id
		queryset2 = Admin.objects.filter(clinic__id = clinicID)
		for e in queryset2:
			notification = ANotification.objects.create(flag='interesse' ,text=time+' '+patientID+' '+medic+' '+clinic+' '+year+'-'+month+'-'+day, admin= e)
		return json_response({'message': 'waiting answer'})


