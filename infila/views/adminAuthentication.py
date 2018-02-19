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

from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token
from infila.serializers import PatientSerializer, AppointSerializer, ClinicSerializer, MedicSerializer, LineSerializer, AdminSerializer, TokenSerializer


@csrf_exempt
def adminLogin(request):
    if request.method == 'POST':
        login = request.POST.get('login', None)
        password = request.POST.get('password', None)
        if login is not None and password is not None:
            try:
                user = Admin.objects.get(login=login)
                if check_password(password, user.password) is not True :
                    user = None
            except Admin.DoesNotExist:
                user = None
            if user is not None:
                if user.is_active:
                    try:
                        token = Token.objects.get(user=user)
                    except Token.DoesNotExist:
                        token = None
                    if token is None:
                        token = Token(user=user)
                        token.save()
                    request.session['adminID'] = user.id
                    return json_response({'token': token.token,'login': user.login,'adminID': user.id})
                else:
                    return json_response({'error': 'Invalid User'}, status=400)
            else:
                return json_response({'error': 'Invalid Username/Password'}, status=400)
        else:
            return json_response({'error': 'Invalid Data'}, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({'error': 'Invalid Method'}, status=405)

@csrf_exempt
@admin_login_required
def adminLogout(request):
    if request.method == 'POST':
        del request.session['adminID']
        return json_response({'status': 'success'})
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({'error': 'Invalid Method'}, status=405)

@csrf_exempt
@admin_login_required
def check(request):
    if request.method == 'POST':
        token = request.POST.get('token', None)
        try:
            tok = Token.objects.get(token=token)
        except Token.DoesNotExist:
            return json_response({'error': 'NOT FOUND'}, status=404)
        if tok.user.id == request.session['adminID']:
            return json_response({'msg':'OK'}, status=200)
        else:
            return json_response({'error': 'incorrect token'}, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({'error': 'Invalid Method'}, status=405)