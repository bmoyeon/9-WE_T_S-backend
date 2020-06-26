import json
import bcrypt
import jwt

from django.views import View
from django.http import (
    HttpResponse,
    JsonResponse
)
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from ami.settings import (
    SECRET_KEY,
    ALGORITHM
)
from .models import (
    Account,
    Guest
)

class AccountSignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            validate_email(data['email'])
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'ALREADY_EXISTS'}, status=401)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            Account.objects.create(
                first_name = data['first_name'],
                last_name  = data['last_name'],
                email      = data['email'],
                password   = hashed_password.decode('utf-8')
            )
            return HttpResponse(status=200)

        except ValidationError:
            return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)

class AccountSignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
                    return JsonResponse({'access_token' : access_token.decode('utf-8')}, status=200)

                return JsonResponse({'message' : 'UNAUTHORIZED'}, status=401)
            return JsonResponse({'message' : 'UNAUTHORIZED'}, status=401)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)

class GuestSignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            validate_email(data['email'])
            Guest.objects.create(email = data['email'])
            return HttpResponse(status=200)

        except ValidationError:
            return JsonResponse({'message' : 'INVALID_EMAIL'}, status=400)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
