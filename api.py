from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import json
load_dotenv()
def getip(ip : str):
    print("fgfhhf")
    request_url = f"http://api.ipstack.com/{ip}?access_key=1bbe4e1dbfa3ba7c37556198453fbaea"
    result = requests.get(request_url).text
    print(result)
    return json.loads(result)




