import sqlite3
from flask import Flask, render_template, jsonify, request
import time, requests

app = Flask(__name__)

@app.route('/')
def post():
    con = sqlite3.connect('data.db')
    c = con.cursor()
    c.execute("SELECT first FROM rng")
    a = c.fetchall()
    fill_a = ''
    for row in a:
        fill_a = fill_a+row[0]+ " " 

    c.execute("SELECT second FROM rng")
    b = c.fetchall()
    fill_b = ''
    for row in b:
        fill_b = fill_b+row[0]+ " " 

    c.execute("SELECT third FROM rng")
    d = c.fetchall()
    fill_c = ''
    for row in d:
        fill_c = fill_c+row[0]+ " "

    return render_template('random.html', ett=fill_a, tva=fill_b, tre=fill_c)
    

if __name__:
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
