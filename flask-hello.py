from flask import Flask

app = Flask(__name__)
x=1

@app.route("/")
def index():
    global x 
    x += 1
    return """<html>
      <title>Secrets</title>
      <body>
        <h1> Lemontime </h1>
        <b>{0}</b> <br/>
        <i>{1}{2}</i> <br/>
      </body>
    </html>""".format("Welcome!","Points:",x)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
