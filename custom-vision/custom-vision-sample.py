
# coding: utf-8

# In[ ]:

import httplib, urllib, base64, json
 
customvisionapi_key = '<<prediction key here>>'
uri_base = 'southcentralus.api.cognitive.microsoft.com'
headers = {
    'Prediction-Key': customvisionapi_key,
    'Content-Type': 'application/json'
}
 

body = "{'Url':