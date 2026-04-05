from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('viewreport/', views.viewreport, name='viewreport'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', include('feedback.urls')),  
]