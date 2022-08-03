from flask import Flask
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def homepage():
    data_set = {
        "Page": "Home",
        "Message": "Successfully loaded homepage",
        "Timestamp": datetime.now()
    }
    
    json_res = json.dumps(data_set, default=str);
    return json_res

@app.route("/about")
def about():
    data_set = {
        "Page": "About",
        "Message": "Successfully loaded about page",
        "Timestamp": datetime.now()
    }
    
    json_res = json.dumps(data_set, default=str);
    return json_res

app.run(host='0.0.0.0', port=80)