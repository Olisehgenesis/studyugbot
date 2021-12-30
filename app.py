
from flask import Flask,

app = Flask(__name__)
from bot import *


@app.route('/{}'.format(secret), methods=["POST"])
def home():
    return getdata