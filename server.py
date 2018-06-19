from flask import Flask, jsonify, Response, request
from flask_cors import CORS, cross_origin
import datetime
import json
import os
import sys
app = Flask(__name__)
CORS(app)

status_file_path = os.path.dirname(__file__) + '/status.json'

@app.route('/')
def status():
    return get_status()

@app.route('/on')
def on():
    command = '/home/pi/pihat --brand=5 --id=' + get_device() + ' --channel=7 --state=1'
    print command
    os.system(command)
    update_status('on')
    return get_status()

@app.route('/off')
def off():
    command = '/home/pi/pihat --brand=5 --id=' + get_device() + ' --channel=6 --state=1'
    print command
    os.system(command)
    update_status('off')
    return get_status()

def update_status(status):
    with open(status_file_path, 'w') as status_file:
        json.dump({'lastCommand': status, 'lastCommandTime': datetime.datetime.now().isoformat()}, status_file)

def get_status():
    with open(status_file_path, 'r') as status_file:
        return Response(status_file.read(), mimetype='application/json')

def get_device():
    try:
        device = str(int(request.args.get('device')))
    except (ValueError, TypeError):
        device = '0'

    return device

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3100)
