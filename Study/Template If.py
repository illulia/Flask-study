from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def helloworld():
    return "Hello Flask World!"

@app.route("/home")
def home():
    return render_template('index(if).html', name = 'Choi')

app.run()