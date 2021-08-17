## **Flask and Docker Application Demo**

Lux Academy &amp; Data Science East Africa Python Boot Camp, Building and Deploying  Flask Application Using Docker Demo App.

Follow 👉🏻 [this](https://docs.docker.com/engine/install/) guide to install docker engine locally in your system

---

**URL With Students  Record:** https://raw.githubusercontent.com/HarunMbaabu/Flask-and-Docker-Application-Domo/main/students.json  

---

--- 
**app.py file:**
---
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

---
Docker File:
---

```dockerfile

FROM python:3.6

COPY . /src


COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 5000

RUN pip install -r requirements.txt


CMD [ "python", "app.py" ]
```

---
**Build docker image called demo:** 
---

```bash
>>> docker build -t demo .  
```

---
**Run docker image called demo:** 
---

```bash
>>>docker run -p 5000:5000 -t -i demo  
```

Now in your local browser visit:   **http://0.0.0.0:5000/students** 


![Preview Image](https://github.com/HarunMbaabu/Flask-and-Docker-Application-Domo/blob/main/src/Screenshot%202021-08-17%20at%2012.40.34.png?raw=true)


