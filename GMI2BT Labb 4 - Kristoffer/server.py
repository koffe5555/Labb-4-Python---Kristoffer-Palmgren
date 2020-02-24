import sqlite3, json, requests
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    content = request.get_json()
    print(f'content: {content}')
    
    
    con = sqlite3.connect('data.db')
    c = con.cursor()
    c.execute("INSERT INTO rng (first, second, third) VALUES (?,?,?)", (content['first'], content['second'], content['third']))

    con.commit()
    con.close()
    return "succes"


app.run(host='0.0.0.0', port=8090)

