from django.urls import path
from .import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('survey/', views.survey, name='survey'),
    path('surveydetail/<emp_no>,<survey_year>', views.surveydetail, name='surveydetail'),
]
