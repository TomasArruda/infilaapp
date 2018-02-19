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

class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

    @detail_route(methods=['get'])
    def appointments(self, request, pk=None):
        queryset = Appointment.objects.filter(line__id=pk)
        serializer = AppointSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)