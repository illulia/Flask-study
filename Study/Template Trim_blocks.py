from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.jinja_env.trim_blocks = True # 이것보단 index.html에서 {%- if name == 'Choi' -%}

@app.route("/")
def helloworld():
    return "Hello Flask World!"

@app.route("/trim")
def trim():
    return render_template('index(if).html', name = 'Choi')

app.run()