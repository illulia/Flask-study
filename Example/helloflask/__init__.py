from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworid():
    return "Hello Flask World!"