from asyncio import subprocess
from flask import Flask, render_template, abort
from flask import request
from flask import jsonify
import datetime
import os
# import utils
# import hit

startTime = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

app = Flask(__name__)

def stdJson(success, msg, data):
    return {
        "success": True if success else False,
        "message": msg,
        "data": data,
    }

def success(msg, data):
    return stdJson(True, msg, data)

def fail(msg, data):
    return stdJson(False, msg, data), 400

@app.route("/")
def home() :
    return render_template("template.html", go="here")

@app.route("/json")
def test() :
    return {
        "key": "v",
        "key2": "v2",
    }

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
