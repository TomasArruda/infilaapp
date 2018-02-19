from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from infila.utils import patient_login_required
from django.http import HttpResponse


from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @list_route()
    def appointments(self, request):
        if 'patientID' not in request.session.keys():
            return HttpResponse('You need to be logged')
        queryset = Appointment.objects.filter(patient__id=request.session['patientID'],line__date__gte=datetime.now(), check = False)
        serializer = AppointSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)

    @list_route()
    def oldAppointments(self, request, pk=None):
        if 'patientID' not in request.session.keys():
            return HttpResponse('You need to be logged')
        queryset = Appointment.objects.filter(patient__id=request.session['patientID'], line__date__lte=datetime.now(), check = True)
        serializer = AppointSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def byPhoneNumber(self, request, pk=None):
        queryset = Patient.objects.filter(phoneNumber=pk)
        serializer = PatientSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)