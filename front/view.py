from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import os.path
from PIL import Image


class SelectCustomerView(View):
    template_name = 'select-customer.html'

    def get(self, request):
        return render(request, self.template_name, {})


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {'current_user': request.user})
        else:
            return redirect('/select-customer/')


class PFProjectLifecycleView(View):
    template_name = 'process-framework/project-lifecycle.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/select-customer/')


class PFSkuCreationView(View):
    template_name = 'process-framework/sku-creation.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/select-customer/')


class PFCoolerOnboardingView(View):
    template_name = 'process-framework/cooler-onboarding.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/select-customer/')


class PFSupportView(View):
    template_name = 'process-framework/support.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/select-customer/')


class PTTimelineHigh(View):
    template_name = 'process-timeline/timeline-high.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/select-customer/')


class PTTimelineDetailed(View):
    template_name = 'process-timeline/timeline-detailed.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/select-customer/')
