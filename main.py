import os
os.system("pip install requests")
import requests
def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Téléchargement terminé :", local_filename)
    else:
        print("Erreur lors du téléchargement :", response.status_code)
os.system("pip install pyyaml")
if not os.path.exists("tempoary"):
    os.makedirs("tempoary")
download_file("https://github.com/EletrixtimeYT/Flask-MonitoringDashboard/releases/download/lastest/Flask_MonitoringDashboard-3.1.1-py3-none-any.whl", "tempoary/Flask_MonitoringDashboard-3.1.1-py3-none-any.whl")
os.system("pip install tempoary/dashboard.whl")
import yaml
import config
print("TimeWeb starting...")

def is_file_allowed(filename):
    exception_path = "config/exception.yaml"
    if os.path.exists(exception_path):
        with open(exception_path, "r") as exception_file:
            exceptions = yaml.safe_load(exception_file)
            if filename in exceptions:
                return False
    return True

if not os.path.exists("dontremoveme.txt"):
    with open("dontremoveme.txt", "w") as txt:
        txt.write("Dont remove me.\n")
        txt.write("You can remove me for an update!\n")
        
    os.system("pip install temp/dashboard.whl")
    print("===========")
    print("Downloader")
    print("===========")
    print("1/5 Installing required packages")
    os.system("pip install flask")
    #os.system("pip install git+https://github.com/eletrixtimeyt/flask-monitoringdashboard")
    
    os.system("pip install pyyaml")
    import requests

 
    download_file("https://github.com/EletrixtimeYT/Flask-MonitoringDashboard/releases/download/lastest/Flask_MonitoringDashboard-3.1.1-py3-none-any.whl", "temp/Flask_MonitoringDashboard-3.1.1-py3-none-any.whl")
    os.system("pip install tempoary/dashboard.whl")
    print("2/5 Creating templates folder")
    if not os.path.exists("public"):
        os.makedirs("public")
    print("3/5 Creating config folder")
    if not os.path.exists("config"):
        os.makedirs("config")
   
        # Créer le fichier exception.yaml s'il n'existe pas
    exception_path = "config/exception.yaml"
    if not os.path.exists(exception_path):
        with open(exception_path, "w") as exception_file:
            temp1 = """
            

# List of files that are not allowed to be accessed\n

#==========================================\n
# #DONT REMOVE IS FOR SAFETY OF THE SERVER\n
- flask_monitoringdashboard.db\n
- main.py\n
- config/exception.yaml\n

#==========================================\n
#Your can add your rules here !\n

#- filename.txt\n
"""
    exception_file.write(temp1)
    response = requests.get("https://raw.githubusercontent.com/EletrixTimeYT/TimeWeb/main/public/index.html")
    response.raise_for_status()
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(response.text)

        


print("4/5 Finishing something...")

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

