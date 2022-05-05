from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import redirect


class LoginView(View):
    template_name = 'signin.html'

    def get(self, request):
        try:
            return render(request, self.template_name)
        except Exception as e:
            print(str(e))
            return JsonResponse({'status': 400, 'message': str(e)})

    def post(self, request):
        post_value = request.POST

        if len(post_value['password']) < 8:
            return JsonResponse({'status': 402, 'message': 'Use 8 characters or more for your password'})
        try:
            validate_email(post_value['email'])
        except:
            return JsonResponse({'status': 403, 'message': 'Email is not valid'})

        user = auth.authenticate(
            request, username=post_value['email'], email=post_value['email'], password=post_value['password'])

        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(0)
            return JsonResponse({'status': 200, 'message': 'Login successfully.'})
        else:
            return JsonResponse({'status': 400, 'message': 'Email or password is incorrect'})


def logout(request):
    auth.logout(request)
    return redirect('/select-customer')
