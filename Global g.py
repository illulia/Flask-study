from flask import Flask, g

app = Flask(__name__)
app.debug = True

@app.before_request #요청하기 이전에 무조건 실행
def before_request():
    print("요청이전!")
    g.str = "한글" #g는 str값으로 "한글"을 가짐

@app.route("/gg")
def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', '111')
                    #기본 속성 가져오는 함수(self,인수,default(기본값 있을때))
@app.route("/")
def helloworld():
    return "Hello Flask World!"

app.run()