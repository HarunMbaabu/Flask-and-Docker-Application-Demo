## **Flask and Docker Application Demo**

Lux Academy &amp; Data Science East Africa Python Boot Camp, Building and Deploying  Flask Application Using Docker Demo App.

> A **Docker image** is a read-only, inert template that comes with instructions for deploying containers. In Docker, everything basically revolves around images.

An image consists of a collection of files (or layers) that pack together all the necessities—such as dependencies, source code, and libraries—needed to set up a completely functional container environment.

> A **Docker container** is a virtualized runtime environment that provides isolation capabilities for separating the execution of applications from the underpinning system. It’s an instance of a Docker image.

**Containers** are the ultimate utility of the Docker technology—they provide a portable and lightweight environment for deploying applications.

Each container is autonomous and runs in its own isolated environment, ensuring it does not disrupt other running applications or its underlying system. This greatly improves the security of applications.


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


