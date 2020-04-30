from flask import Flask, request, Response, make_response

app = Flask(__name__) #__main__이 들어가게됨
app. debug = True

@app.route("/") #도메인 경로 지정
def helloworld():
    return "Hello Flask World!" #response해줌

@app.route("/ro")
def ro():
    res = Response("Test")
    res.headers.add('Program-Name','Test Response')
    res.set_data("This is Test Program.")
    res.set_cookie("UserToken","A12Bc9")
    return make_response(res)

app.run()