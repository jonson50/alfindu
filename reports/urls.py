from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports, name='reports'),
    path('<int:pk>/download/report/', views.report_download, name='download_report'),
]
