from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
#app.config["DEBUG"] = False

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')

@app.route("/img")
def img():
    return render_template('img.html')
    
if __name__ == '__main__':
    app.run(debug=True)

