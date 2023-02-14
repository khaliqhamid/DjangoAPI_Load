from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    # api_request= requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_96563a291e3c494ea7ec034295e639f9")
    api_request= requests.get("https://portal.gulfcable.com:8443/API/Survey/GetEmpSurveyResponse?empNo=02217&surveyYear=2022-01")
    # api_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=IT&departmentId=&status=Surveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2022-01")
    
   
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        # api.raise_for_status()
        api="Error, data not loading"    
    
    return render(request, 'index.html', {'api':api})


def test(request):
    return render(request, 'test.html')


def survey(request):
    # surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=IT&departmentId=&status=Surveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2022-01")
    surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=NULL&departmentId=&status=Surveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2022-01")

    try:
        surveyApi = json.loads(surveyApi_request.content)

    except Exception as e:
        surveyApi =  "Error, data not loading"

    return render(request, 'surveylist.html', {'surveyApi': surveyApi})
    