from flask import Flask, jsonify, Response, request
from flask_cors import CORS, cross_origin
import datetime
import json
import os
import sys
app = Flask(__name__)
CORS(app)

status_file_path_template = os.path.dirname(__file__) + '/status_device_%s.json'

@app.route('/')
def status():
    device = get_device()
    return get_status(device)

@app.route('/on')
def on():
    device = get_device()
    command = get_command(device, True)
    print command
    os.system(command)
    update_status(device, 'on')
    return get_status(device)

@app.route('/off')
def off():
    device = get_device()
    command = get_command(device, False)
    print command
    os.system(command)
    update_status(device, 'off')
    return get_status(device)

def get_status(device):
    status_file_path = status_file_path_template % (device)
    with open(status_file_path, 'r') as status_file:
        return Response(status_file.read(), mimetype='application/json')

def update_status(device, status):
    status_file_path = status_file_path_template % (device)
    with open(status_file_path, 'w') as status_file:
        json.dump({'lastCommand': status, 'lastCommandTime': datetime.datetime.now().isoformat()}, status_file)

def get_device():
    """Gets a string to identify the device

    Returns:
        str: Device string provided in URL, or '0' as a default
    """
    try:
        device = str(int(request.args.get('device')))
    except (ValueError, TypeError):
        device = '0'

    return device

def get_command(device, status):
    """Gets the pihat command to run

    Args:
        device (str): device ID, e.g. '0'
        status (bool): whether to turn on or off
    Returns:
        str: Command
    """
    channel = '7' if status else '6'

    return '/home/pi/pihat/pihat --brand=5 --id=' + device + ' --channel=' + channel + ' --state=1'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3100, threaded=True)
