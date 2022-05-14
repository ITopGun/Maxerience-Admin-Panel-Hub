from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from front.models import Documents
import os.path
from PIL import Image
from django.http import QueryDict


class TDSolutionView(View):
    template_name = 'technical-documentation/solution.html'

    def get(self, request):
        page_name = 'solution'
        documents = Documents.objects.filter(page_name=page_name)
        results = []
        for document in documents:
            results.append({
                "title": document.title,
                "description": document.description,
                "path": document.file,
                "id": document.id
            })
        if request.user.is_authenticated:
            return render(request, self.template_name, {"results": results, "page_name": page_name})
        else:
            return redirect('/select-customer/')

    def post(self, request):
        try:
            current_user = request.user
            post_value = request.POST
            dir = ''
            document = {}

            if request.FILES and request.FILES['file']:
                document = Documents.objects.create(
                    title=request.FILES['file'].name, description=post_value['description'], page_name=post_value['page_name'])
                document.file = request.FILES['file']
                document.save()
                dir = document.file.url
            else:
                return JsonResponse({'status': 400, 'message': 'Invalid File.'})

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'title': request.FILES['file'].name, 'description': post_value['description'], 'dir': dir, 'id': document.id})

    def delete(self, request, id):
        try:
            current_user = request.user
            del_value = QueryDict(request.body)
            del_id = del_value.get('id')
            document = Documents.objects.filter(id=id)
            document.delete()

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': 'Deleted successfully'})
        