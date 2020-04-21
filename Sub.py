from flask import Flask

app = Flask(__name__)
app.debug = True
app.config['SERVER_NAME'] = 'local.com:5000'

@app.route("/")
def helloworld():
    return "Hello Flask World!"

@app.route("/",subdomain="g")
def hellogworld():
    return "Hello G.Local.com!"

app.run()