from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from front.models import Documents
import os.path
from PIL import Image
from django.http import QueryDict
import json


class UserManagementView(View):
    template_name = 'user-management.html'

    def get(self, request):
        page_name = 'user-management'
        users = User.objects.all()
        if request.user.is_authenticated:
            return render(request, self.template_name, {"users": users})
        else:
            return redirect('/select-customer/')

    def put(self, request, id):
        try:
            current_user = request.user
            post_value = request.POST
            put_value = QueryDict(request.body)
            is_active = put_value.get('is_active')
            is_staff = put_value.get('is_staff')
            user = User.objects.filter(id=id)[0]
            user.is_active = is_active
            user.is_staff = is_staff
            user.save()

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': f'{user.username} updated successfully.'})

    def delete(self, request, id):
        try:
            current_user = request.user
            del_value = QueryDict(request.body)
            del_id = del_value.get('id')
            del_id = json.loads(del_id)
            print(del_id)
            user = User.objects.filter(id__in=del_id)
            user.delete()

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': f'Users deleted successfully'})
