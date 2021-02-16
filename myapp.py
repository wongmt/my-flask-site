from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/myprivacy")
def myprivacy():
    return render_template('privacy.html')

@app.route("/img")
def img():
    return render_template('img.html')
    
if __name__ == '__main__':
    app.run(debug=True)
