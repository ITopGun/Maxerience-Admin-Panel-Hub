from django.urls import path

from .views.auth import login, signup
from .view import IndexView, PFProjectLifecycleView, PFSkuCreationView, PFCoolerOnboardingView, PFSupportView, PTTimelineHigh, PTTimelineDetailed, SelectCustomerView
from .views.checklists import project, masterDataModel, mobileWebApps, paymentIntegration, installationConfig, materialList, coolerOnboarding, coolerHealthCheck, dashboards
from .views.technicalDocumentation import solution, installationManual, tdcoolerOnboarding, transaction, operational, tdcoolerHealthCheck
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='user_login'),
    path('logout/', login.logout, name='user_logout'),
    path('signup/', signup.SignUpView.as_view(), name='user_signup'),
    path('', IndexView.as_view(), name='index'),
    path('select-customer/', SelectCustomerView.as_view(), name="select_customer"),


    # Process Framework Pages
    path('project-lifecycle/', PFProjectLifecycleView.as_view(),
         name='project_lifecycle'),
    path('sku-creation/', PFSkuCreationView.as_view(), name='sku_creation'),
    path('cooler-onboarding/', PFCoolerOnboardingView.as_view(),
         name='cooler_onboarding'),
    path('support/', PFSupportView.as_view(), name='support'),


    # Process Timeline Pages
    path('timeline-high/', PTTimelineHigh.as_view(), name='timeline_high'),
    path('timeline-detailed/', PTTimelineDetailed.as_view(),
         name='timeline_detailed'),


    # Checklists Pages
    path('project/', project.ChecklistsProjectView.as_view(), name='project'),
    path('master-data-model/', masterDataModel.ChecklistsMasterDataModelView.as_view(),
         name='master_data_model'),
    path('mobile-web-apps/', mobileWebApps.ChecklistsMobileWebAppsView.as_view(),
         name='mobile_web_apps'),
    path('payment-integration/', paymentIntegration.ChecklistsPaymentIntegrationView.as_view(),
         name='payment_integration'),
    path('install-config/', installationConfig.ChecklistsInstallationConfigView.as_view(),
         name='install_config'),
    path('material-list/', materialList.ChecklistsMaterialListView.as_view(),
         name='material_list'),
    path('checklist-cooler-onboarding/', coolerOnboarding.ChecklistsCoolerOnboardingView.as_view(),
         name='checklist_cooler_onboarding'),
    path('cooler-health-check/', coolerHealthCheck.ChecklistsCoolerHealthCheckView.as_view(),
         name='cooler_health_check'),
    path('dashboards/', dashboards.ChecklistsDashboardsView.as_view(),
         name='dashboards'),


    # Technical Documentation Pages
    path('solution/', solution.TDSolutionView.as_view(), name='timeline_high'),
    path('installation-manual/', installationManual.TDInstallationManualView.as_view(),
         name='timeline_detailed'),
    path('technical-cooler-onboarding/',
         tdcoolerOnboarding.TDCoolerOnboardingView.as_view(), name='timeline_high'),
    path('transaction/', transaction.TDTransactionView.as_view(),
         name='timeline_detailed'),
    path('operational/', operational.TDOperationalView.as_view(),
         name='timeline_high'),
    path('technical-cooler-health-check/', tdcoolerHealthCheck.TDCoolerHealthCheckView.as_view(),
         name='timeline_detailed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
