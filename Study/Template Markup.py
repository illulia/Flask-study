from flask import Flask, render_template, Markup

app = Flask(__name__)
app.debug = True

@app.route("/")
def helloworld():
    return Markup("<h1>Makrup test</h1>")

@app.route("/mkup")
def mkup():
    title = Markup("<strong>Use Markup : This is Markup Test<strong>")
    mu = Markup("<h1>10 + 5 = <i>%s</i></h1>")
    h = mu % "15"
    return render_template('index(Markup).html', tit=title, sum=h)

app.run()