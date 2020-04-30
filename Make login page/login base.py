from flask import Flask, render_template, redirect 
from flask import request , Response

app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route("/")
def main(ID=None):
    return render_template('login main.html', ID=ID)

@app.route("/home")
def home():
    return render_template('login complete.html')

@app.route("/error")
def error():
    return render_template('login error.html')

@app.route("/lp", methods = ['POST', 'GET'])
def lp():
    a = 'c'
    b = 'c'
    id1 = request.args.get("ID")
    pw1 = request.args.get("PW")
    if id1 == a and pw1 == b:
        return redirect('/home')
    else:
        return redirect('/error')

app.run() 