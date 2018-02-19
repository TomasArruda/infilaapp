from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.views.decorators.csrf import csrf_exempt


from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, PNotification, ANotification
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer, PNotificationSerializer, ANotificationSerializer

class ANotificationViewSet(viewsets.ModelViewSet):
    queryset = ANotification.objects.all()
    serializer_class = ANotificationSerializer

    @detail_route(methods=['get'])
    def byAdminID(self, request, pk=None):
        queryset = ANotification.objects.filter(admin__id=pk)
        serializer = ANotificationSerializer(queryset,many=True, context={'request': request})
        return Response(serializer.data)


