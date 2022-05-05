from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from front.models import Documents
import os.path
from PIL import Image


class TDTransactionView(View):
    template_name = 'technical-documentation/solution.html'

    def get(self, request):
        page_name = 'transaction'
        documents = Documents.objects.filter(page_name=page_name)
        results = []
        for document in documents:
            results.append({
                "title": document.title,
                "description": document.description,
                "path": document.file
            })
        if request.user.is_authenticated:
            return render(request, self.template_name, {"results": results, "page_name": page_name})
        else:
            return redirect('/select-customer/')
