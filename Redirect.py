from flask import Flask, redirect

app = Flask(__name__)
app.debug = True

@app.route("/")
def helloworld():
    return "Hello Flask World!"

@app.route("/re")
def re():
    return redirect('/con')

@app.route("/con")
def con():
    return "Redirect Sucess"

app.run()