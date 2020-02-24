"""env FLASK_APP=program.py FLASK_ENV=development flask run"""

from flask import Flask, render_template, jsonify
from flask import request
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def echo():
    user = [
    request.form.get('fname'),
    request.form.get('ename'),
    request.form.get('address'),
    request.form.get('zipcode'),
    request.form.get('city'),
    request.form.get('cellphone'),
    request.form.get('email'),
    request.form.get('pw'),
    request.form.get('payment'),
    request.form.get('offers'),
    request.form.get('format'),
    request.form.get('comment')]

    f_name = user[0]
    e_name = user[1]
    address = user[2]
    postnmr = user[3]
    stad = user[4]
    telnmr = user[5]
    email = user[6]
    pw = user[7]
    betala = user[8]
    offer = user[9]
    form = user[10]
    kommentar = user[11]
    return render_template('index.html', fname=f_name, ename=e_name, address=address, postnmr=postnmr, ort=stad, mobil=telnmr, email=email, pw=pw, pay=betala, offer=offer, val=form, kommentar=kommentar)
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

