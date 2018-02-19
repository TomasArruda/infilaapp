from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.views.decorators.csrf import csrf_exempt


from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer

class ClinicViewSet(viewsets.ModelViewSet):
	queryset = Clinic.objects.all()
	serializer_class = ClinicSerializer

	@detail_route(methods=['post'])
	def signUpMedic (self, request, pk=None):
		medicID = request.GET.get('medicID', '')
		clinic = Clinic.objects.get(id = pk)
		medic = Medic.objects.get(id = medicID)
		clinic.medics.add(medic)
		return Response({'message': 'medic added successfully'})


