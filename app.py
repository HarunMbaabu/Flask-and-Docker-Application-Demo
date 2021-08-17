import requests
from flask import Flask,jsonify

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
    app.run(debug=True)      
