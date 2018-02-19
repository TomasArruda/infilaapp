from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.views.decorators.csrf import csrf_exempt
from infila.utils import *
from django.contrib.auth.hashers import *
from django.contrib.auth import login

from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, PToken
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer, PTokenSerializer

#TOTEST
@csrf_exempt
def patientLogin(request):
    if request.method == 'POST':
        phoneNumber = request.POST.get('phoneNumber', None)
        password = request.POST.get('password', None)
        print request
        print phoneNumber
        print password
        if phoneNumber is not None and password is not None:
            try:
                user = Patient.objects.get(phoneNumber=phoneNumber)
                if check_password(password, user.password) is not True :
                    user = None
            except Patient.DoesNotExist:
                user = None
            if user is not None:
                if user.is_active:
                    try:
                        token = PToken.objects.get(user=user)
                    except PToken.DoesNotExist:
                        token = None
                    if token is None:
                        token = PToken(user=user)
                        token.save()
                    request.session['patientID'] = user.id
                    return json_response({'token': token.token,'patientID': user.id})
                else:
                    return json_response({'error': 'Invalid User'}, status=400)
            else:
                return json_response({'error': 'Invalid Username/Password','phoneNumber': phoneNumber,'password': password}, status=400)
        else:
            return json_response({'error': 'Invalid Data'}, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({'error': 'Invalid Method'}, status=405)


@csrf_exempt
@patient_login_required
def patientLogout(request):
    if request.method == 'POST':
        #request.token.delete()
        del request.session['patientID']
        return json_response({'status': 'success'})
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({'error': 'Invalid Method'}, status=405)


@csrf_exempt
@patient_login_required
def pcheck(request):
    if request.method == 'POST':
        token = request.POST.get('token', None)
        try:
            tok = PToken.objects.get(token=token)
        except PToken.DoesNotExist:
            return json_response({'error': 'NOT FOUND'}, status=404)
        if tok.user.id == request.session['patientID']:
            return json_response({'msg':'OK'}, status=200)
        else:
            return json_response({'error': 'incorrect token'}, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({'error': 'Invalid Method'}, status=405)