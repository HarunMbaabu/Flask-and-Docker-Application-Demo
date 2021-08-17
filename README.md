# Flask and Docker Application Demo


Lux Academy &amp; Data Science East Africa Python Boot Camp, Building and Deploying  Flask Application Using Docker Demo App.


**URL With Students  Record:** https://raw.githubusercontent.com/HarunMbaabu/Flask-and-Docker-Application-Domo/main/students.json  


**app.py file:**

```python 
import requests
from flask import Flask, jsonify

app = Flask(__name__)

api_url = "https://raw.githubusercontent.com/HarunMbaabu/Flask-and-Docker-Application-Domo/main/students.json"

@app.route("/students")
def get_json_data():
    try:
      api_response = requests.get(api_url)
      json_dict = api_response.json()
      return jsonify(json_dict)
    except Exception as e:
      print("Error occured :: %s" % e.message) 


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")    

```


Docker File:

```dockerfile

FROM python:3.6

COPY . /src


COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 5000

RUN pip install -r requirements.txt


CMD [ "python", "app.py" ]
```








