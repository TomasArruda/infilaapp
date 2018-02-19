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

from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer

class MedicViewSet(viewsets.ModelViewSet):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer

    @detail_route(methods=['get'])
    def appointments(self, request, pk=None):
        queryset = Appointment.objects.filter(line__medic__id=pk)
        serializer = AppointSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def todaysAppointments(self, request, pk=None):
        queryset = Appointment.objects.filter(line__medic__id=pk, line__date=datetime.now())
        serializer = AppointSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def lines(self, request, pk=None):
        queryset = Line.objects.filter(medic__id=pk)
        serializer = LineSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)