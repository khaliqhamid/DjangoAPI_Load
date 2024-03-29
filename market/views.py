from django.shortcuts import render
import requests
import json
# Create your views here.


def verify(request):
    if request.method =="POST":
        empno = request.POST.get('EmployeeNo')
        
        # parameters = {
        #    "status": empno,
        # }
        # emp_no = f"{empno:05d}" 
        padded_num = '{:0>5}'.format(empno)
        
        # verifyEmp = requests.get("https://portal.gulfcable.com:8443/api/Survey/ValidateEmployee", params = parameters)
        verifyEmp = requests.get("https://portal.gulfcable.com:8443/api/Survey/ValidateEmployee?empNo=" + padded_num)
        # verifyEmp = requests.get("https://portal.gulfcable.com:8443/api/Survey/ValidateEmployee?empNo=02217")
   
        try:
            userInfo = json.loads(verifyEmp.content)
            # if user.isValidEmpNo true:
                
            #     user= "Data not found"
            
        except Exception as e:
            # api.raise_for_status()
            userApi = "Error, data not loading"   
   
        return render(request, 'OTP.html', {'userApi': userInfo})
    else:
        return render(request, 'verify.html')

    

def index(request):
    return render(request, 'index.html')
     

def index2(request):
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


# def survey(request):
#     # surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=IT&departmentId=&status=NotSurveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2022-01")
#     surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=NULL&departmentId=&status=Surveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2022-01")
#     # surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=IT&departmentId=&status=Not Surveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2022-01")
    
#     try:
#         surveyApi = json.loads(surveyApi_request.content)

#     except Exception as e:
#         surveyApi =  "Error, data not loading"

#     return render(request, 'survey.html', {'surveyApi': surveyApi})
    
    
    
# def survey(request, status, surveyYear):
# def survey(request, status):
def survey(request):
    if request.method=="POST":
        status = request.POST.get('surveyStatus')
        
        parameters = {
           "status": status,
            "SurveyYear":"2021-01"
        }
        
        # surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=NULL&departmentId=&status=" + status + "&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2021-01" )
        surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2",params=parameters )
        try:
              surveyApi = json.loads(surveyApi_request.content)
        except Exception as e:
             surveyApi =  "Error, data not loading"
        return render(request, 'survey.html', {'surveyApi': surveyApi})    
    
    else:
        # surveyApi =  "Error, data not loading"
        surveyApi_request = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetSurveyStatusV2?department=NULL&departmentId=&status=surveyed&question&questionId=0&chartQuestionLabel=&chartFor=&SurveyYear=2021-01" )
        try:
              surveyApi = json.loads(surveyApi_request.content)
        except Exception as e:
             surveyApi =  "Error, data not loading"
        return render(request, 'survey.html', {'surveyApi': surveyApi})     
    
    
    
# def surveydetail(request, emp_no):
#     surveyDetail = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetEmpSurveyResponse?empNo=" + emp_no + "&surveyYear=2021-01")
def surveydetail(request, emp_no, survey_year):
    surveyDetail = requests.get("https://portal.gulfcable.com:8443/API/Survey/GetEmpSurveyResponse?empNo=" + emp_no + "&surveyYear="+ survey_year )
    
    try:
        survey = json.loads(surveyDetail.content)

    except Exception as e:
                    survey =  "Error, data not loading"

    return render(request, 'surveydetail.html', {'surveydetail': survey})