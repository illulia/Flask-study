from flask import Flask, request, Response, make_response

app = Flask(__name__)
app.debug = True

@app.route("/") 
def helloworld():
    return "Hello Flask World!"

@app.route("/wc")
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    return make_response(res)

@app.route("/rc")
def rc():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return "cookie[" + key + "] = " + val


app.run()