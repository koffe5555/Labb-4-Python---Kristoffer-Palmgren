import sqlite3, time, json, requests
from flask import Flask, request
from random import randint
from flask import Flask, render_template, jsonify

while True:
    n = randint(1, 99)
    m = randint(1, 99)
    b = randint(1, 99)
    data_dict = {"first": n, "second": m, "third": b}
    r = requests.post('http://localhost:8090/postjson', json=data_dict)
    time.sleep(10)
    

