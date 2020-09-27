from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask import abort

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def get_status ():
    return jsonify({"status": "running"}), 200
