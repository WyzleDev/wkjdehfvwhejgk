from flask import Flask
import requests
import shutil
import os
app = Flask(__name__)
from printDocument import *

cookie = {}

def setup():
    log = requests.post(f"http://192.168.0.137:33380/api/login?database=v_24&password=module")
    log_r = f"{log.headers['Set-Cookie']}"

    cookie["Cookie"] = log_r


@app.get("/print/recruit/<int:id>")
def print_route(id):
    USER_PATH = os.path.expanduser("~")
    ck = f"{cookie['Cookie']}"
    headers = {"Cookie": f"{ck}"}
    r = requests.get(f"http://192.168.0.137:33380/api/reports/recruits/ZIC?recruitId={id}", headers=headers, stream=True)

    with open(f"{USER_PATH}/Documents/{id}.docx", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

    printWordDocument(f"{USER_PATH}\\Documents\\{id}.docx")

    return "<p>Done</p>"




setup()
app.run(host='0.0.0.0', port=5000)