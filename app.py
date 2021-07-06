from flask import Flask, render_template

import requests
import json


app = Flask(__name__)

BASE = "http://127.0.0.1:5000/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vehicle/<vehicle_number>")
def get_info(vehicle_number):
    response = requests.get(BASE + "vehicle/" + vehicle_number)
    return render_template("ownerInfo.html", response=response)

# print(json.dumps(response.json(), indent=1))
if __name__=="__main__":
    app.run(debug=True, host="192.168.153.207", port=8080)