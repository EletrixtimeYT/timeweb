import os
import yaml
import requests
import config
def is_file_allowed(filename):
    exception_path = "config/exception.yaml"
    if os.path.exists(exception_path):
        with open(exception_path, "r") as exception_file:
            exceptions = yaml.safe_load(exception_file)
            if filename in exceptions:
                return False
    return True
        




print("5/5 Starting...")
print("NOTE: Put HTML files in the templates folder!")

from flask import Flask, send_file, abort 
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.bind(app)

@app.route('/<path:filename>')  # Use a dynamic path to capture the entire path after "/"
def get_asset(filename):
    if not is_file_allowed(filename):
        return abort(401)  # Return a 401 error if the file is in the exceptions list
    
    public_filename = os.path.join("public", filename)
    return send_file(public_filename)
@app.route('/')
def index():
    return send_file("public/index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.port)

