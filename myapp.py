from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = False

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

import os
from flask_sqlalchemy import SQLAlchemy


import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']	
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
     
    # A constructor function 
    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content
        
@app.route("/blog")
def blog():
    #post_data = Post.query.all()
    #return render_template("blog.html", post_data = post_data)
    cur = conn.cursor()
    cur.execute('select * from blog;' )
    conn.commit()
    cur.close()
    conn.close()
    
if __name__=="__main__":
    app.run(debug=False)
 