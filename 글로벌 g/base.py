from flask import Flask, g

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    print("요청이전!")
    g.str = "한글"

@app.route("/gg")
def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', '111')

@app.route("/")
def helloworld():
    return "Hello Flask World!"

app.run()