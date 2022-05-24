from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            post_value = request.POST

            if post_value['password'] != post_value['cpassword']:
                return JsonResponse({'status': 401, 'message': 'Passwords do not match'})
            if len(post_value['password']) < 8:
                return JsonResponse({'status': 402, 'message': 'Use 8 characters or more for your password'})
            try:
                validate_email(post_value['email'])
            except:
                return JsonResponse({'status': 403, 'message': 'Email is not valid'})

            if User.objects.filter(username=post_value['email']).exists():
                return JsonResponse({'status': 404, 'message': 'Email already exists'})

            user = User.objects.create_user(
                username=post_value['email'], email=post_value['email'], password=post_value['password'], is_active=0)

            user.save()

            # auth.login(request, user)
            request.session.set_expiry(0)

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': 'You are registered successfully.'})
