#!/usr/bin/python

from flask import Flask
from flask import request
import logging
from logging.handlers import RotatingFileHandler
from subprocess import call

import pprint
pp = pprint.PrettyPrinter(indent=4)
app = Flask(__name__)
@app.route('/eventbus', methods=['POST'])
def eventbus():
    json = request.get_json()
    app.logger.info(pprint.pformat(json, indent=4))
    if 'eventType' in json and 'taskStatus' in json:
        if json['eventType'] == 'status_update_event' and json['taskStatus'] == 'TASK_RUNNING':    
#    if hasattr(json, 'eventType')  and hasattr(json,'taskStatus'):
#        if json.eventType == 'status_update_event' and json.taskStatus == 'TASK_RUNNING':
            app.logger.info("Calling update_nginx.sh")
            call(["/opt/shim/update_nginx.sh",json['appId'], json['host'], str(json['ports'][0])])
#        if json.eventType == 'app_terminated_event':
#            app.logger.info("Calling update_nginx.sh")
#            call(["./update_nginx.sh",json.appId, json.host, json.ports[0]])
    return ('', 204)
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    handler = RotatingFileHandler('shim.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.debug = True
    app.run()
