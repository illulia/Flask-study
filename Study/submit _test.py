from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@app.route('/')
def main_get(num=None):
    return render_template('submit.html', num=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    # if request.method == 'POST':
        #pass
    if request.method == 'GET':
        temp = request.args.get('num')
        temp = int(temp)
        temp1 = request.args.get('char1')
        return render_template('submit.html', num=temp, char1=temp1)

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
