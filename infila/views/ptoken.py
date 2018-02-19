from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.views.decorators.csrf import csrf_exempt


from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, PToken
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer, PTokenSerializer

class PTokenViewSet(viewsets.ModelViewSet):
    queryset = PToken.objects.all()
    serializer_class = PTokenSerializer