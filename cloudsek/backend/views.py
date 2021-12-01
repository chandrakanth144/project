import django
django.setup()
from django.http.response import HttpResponse, Http404
import time
from .models import *
from multiprocessing import Process
from django.shortcuts import render
import requests
import json


# Create your views here.

def home(request):
    context ={}
    context ['testvar'] = "hello"
    consumer_key= "3MVG9pRzvMkjMb6m5z4Hbj2oMNdOB7gTWTJKTzqdfsHVrTwIAPNaMr.vqIbloenO1ootARtM6lbXZz6aztd4X"
    consumer_secret = "D588CDA1079259B935CC4E2DE7E0C301C2EDC896374DC7DBFF296CB358D22AD6"
    username="mohanchandra.a77-ujwp@force.com"
    password="123qweasd"
    security_token = ""
    payload = {
        'grant_type': 'password',
        'client_id': consumer_key,
        'client_secret': consumer_secret,
        'username': username,
        'password': password,
    }
    r = requests.post("https://login.salesforce.com/services/oauth2/token",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data=payload)
    print(r.content)
    jsn = json.loads(r.content)
    access_token = jsn["access_token"]
    instance_url = jsn["instance_url"]
    token_type = jsn["token_type"]
    issued_at = jsn["issued_at"]
    signature = jsn["signature"]
    id = jsn["id"]
    data = calculate(access_token=access_token, instance_url=instance_url, token_type=token_type, issued_at=issued_at, signature=signature, token_id=id)
    data.save()
    # i was getting errors from here so i just did the above part 
    """rr = requests.post(instance_url+"/services/data/v20.0/query/?q=SELECT+name+from+Account",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},)
    print(rr.content)"""
    return render(request, 'home.html')
