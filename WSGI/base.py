from flask import Flask, g, Response, make_response

app = Flask(__name__)
app.debug = True 

@app.route('/test_wsgi') # Web Server Gateway Interface 
def wsgi_test(): # (environ)flask의 환경변수 담음 (start_response)는 function
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/html'),
                    ('Content-Length',str(len(body)))] # headers 튜플을 담은 리스트 형태
        start_response('200 OK', headers)
        return [body]
    
    return make_response(application)
                
@app.route("/")
def helloworld():
    return "Hello Flask World!"

app.run()