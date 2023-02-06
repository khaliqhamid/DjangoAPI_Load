from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    api_request= requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_96563a291e3c494ea7ec034295e639f9")
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api="Error, data not loading"    
    
    return render(request, 'index.html', {'api':api})

# https://cloud.iexapis.com/stable/tops?token=YOUR_TOKEN_HERE&symbols=aapl