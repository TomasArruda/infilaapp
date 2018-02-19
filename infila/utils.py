import json
from django.http import HttpResponse



def json_response(response_dict, status=200):
    response = HttpResponse(json.dumps(response_dict), content_type="application/json", status=status)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

#def token_required(func):
#    def inner(request, *args, **kwargs):
#        if request.method == 'OPTIONS':
#            return func(request, *args, **kwargs)
#        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
#        if auth_header is not None:
#            tokens = auth_header.split(' ')
#            if len(tokens) == 2 and tokens[0] == 'Token':
#                token = tokens[1]
#                try:
#                    request.token = Token.objects.get(token=token)
#                    return func(request, *args, **kwargs)
#                except Token.DoesNotExist:
#                    return json_response({'error': 'Token not found'}, status=401)
#        return json_response({'error': 'Invalid Header'}, status=401)
#    return inner

def admin_login_required(func):
    def inner(request, *args, **kwargs):
        if 'adminID' not in request.session.keys():
            return json_response({'error': 'you must log in to access this'}, status=401)
        return func(request, *args, **kwargs)
    return inner

def patient_login_required(func):
    def inner(request, *args, **kwargs):
        if 'patientID' not in request.session.keys():
            return json_response({'error': 'you must log in to access this'}, status=401)
        return func(request, *args, **kwargs)
    return inner
