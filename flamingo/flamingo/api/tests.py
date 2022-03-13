from urllib import request
from django.test import TestCase
import requests


url= "http://127.0.0.1:8000/api/insert"
params= {'timestamp':'2022-01-02', 
         'value': '2'
         }
res= requests.get(url, params= params)
print(res.json())
print(res.status_code, end='\n\n')


url= "http://127.0.0.1:8000/api/graph"
res= requests.get(url)
print(res.json())
print(res.status_code)

