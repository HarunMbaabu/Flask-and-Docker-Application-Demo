# Flask and Docker Application Demo


Lux Academy &amp; Data Science East Africa Python Boot Camp, Building and Deploying  Flask Application Using Docker Demo App.


Docker File:

**URL With Students  Record:** https://raw.githubusercontent.com/HarunMbaabu/Flask-and-Docker-Application-Domo/main/students.json  



```dockerfile

FROM python:3.6

COPY . /src


COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 5000

RUN pip install -r requirements.txt


CMD [ "python", "app.py" ]
```








