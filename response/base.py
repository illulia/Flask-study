from flask import Flask, g, Response, make_response

app = Flask(__name__)
app.debug = True 

@app.route('/res1')
def res1():                               # status # 헤더에 은밀한값 보내기
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)
          #큰 파일이나 데이터 보낼때 더 가벼움 (밑에 코드 보다)
@app.route("/gg")
def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', '111')
                
@app.route("/")
def helloworld():
    return "Hello Flask World!"

app.run()