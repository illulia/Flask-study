from flask import Flask

app = Flask(__name__) #__main__이 들어가게됨
app.debug = True

@app.route("/") #도메인 경로 지정
def helloworld():
    return "Hello Flask World!" #response해줌

app.run()