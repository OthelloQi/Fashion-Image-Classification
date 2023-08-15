
# coding: utf-8

# In[ ]:

import httplib, urllib, base64, json
 
customvisionapi_key = '<<prediction key here>>'
uri_base = 'southcentralus.api.cognitive.microsoft.com'
headers = {
    'Prediction-Key': customvisionapi_key,
    'Content-Type': 'application/json'
}
 

body = "{'Url': 'https://raw.githubusercontent.com/amynic/deep-learning-fashion/master/dataset/test/0label_image10007.png'}"
# All images are listed here: https://github.com/amynic/deep-learning-fashion/tree/master/dataset/test 
# change the filename to test different files
 
#enter everything after - https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/ as custom_vision_url variable
 
custom_vision_url = "<projectid>/url?iterationId=<iterationid>" 
 
try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection(uri_base)
    conn.request("