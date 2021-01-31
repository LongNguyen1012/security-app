import sys
sys.path.insert(0, 'D:\\dockernodejs\\')

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

from flask import Flask
from ec2SDKPython.test import start_vm, stop_vm
from dockerSDKpython.dockercheck import DockerControl

run_cont = DockerControl()
app = Flask(__name__)


@app.route('/health')
def health():
    return 'Hello, World!'


@app.route('/start-vm')
def start():
    res = start_vm()
    return res 


@app.route('/stop-vm')
def stop():
    res = stop_vm()
    return res 


@app.route('/start-container')
def start_cont(): 
    # To run a container named "alpine"
    run_cont.pull_image('alpine')
    res = run_cont.run_container('alpine', ["echo", "hello", "world"])
    return res


# To stop a continer
@app.route('/stop-container')
def stop_cont(): 
    # To stop a container named "alpine"
    run_cont.stop_container('alpine')
    return "container stopped"


# To list continers
@app.route('/list-container')
def list_cont(): 
    # To stop a container named "alpine"
    return tuple(run_cont.list_container())


if __name__ == '__main__':
   app.run(debug = True)