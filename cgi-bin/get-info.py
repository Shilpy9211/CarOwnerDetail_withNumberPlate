#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import requests
import json
import subprocess as sb
from flask import render_template
#vehicle_number = sb.getoutput("python3 predictor.py")

vehicle_number = 'MH01AV8866'
BASE = 'http://127.0.0.1:5000/'

# field = cgi.FieldStorage()
# vehicle_number = field.getvalue("vehicle_number")


response = requests.get(BASE + "vehicle/" + vehicle_number)
print(json.dumps(response.json(), indent=1))
