from django.urls import path
from .import views

urlpatterns = [
    path('verify/', views.verify, name='verify'),
    
    path('index/', views.index, name='index'),
    path('', views.index2, name='index2'),
    path('test/', views.test, name='test'),
    path('survey/', views.survey, name='survey'),
    # path('survey/<status>', views.survey, name='survey'),
    path('surveydetail/<emp_no>/<survey_year>', views.surveydetail, name='surveydetail'),
]
