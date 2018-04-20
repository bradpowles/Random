from flask import Flask, render_template, request, redirect, url_for
from data import data
try:
    import PyQt5
except:
    print("What a shame . . .")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signinfo')
def signinfo():
    zsign = str(request.args.get("sign", None))
    if zsign in data:
        fact = data[zsign]['fact']
        return render_template('signinfo.html', sign=zsign.upper(), fact=fact)
    else:
        return "That is not a Zodiac Sign!"


@app.route('/_getsign', methods=['POST'])
def _getsign():
    date = int(request.form['date'])
    month = int(request.form['month'])
    sign = None
    for i in data:
        if data[i]['start_range'][1] == month:
            if data[i]['start_range'][0] <= date:
                sign = data[i]["name"]
        if data[i]['end_range'][1] == month:
            if data[i]['end_range'][0] >= date:
                sign = data[i]["name"]
    return redirect(url_for('signinfo', sign=sign))


if __name__ == "__main__":
    app.run()
