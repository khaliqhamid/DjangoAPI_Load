from django.urls import path
from .import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('surveylist/', views.survey, name='surveylist'),
    
]
