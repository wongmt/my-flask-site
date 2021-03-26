from flask import Flask, render_template
import sqlite3

import os
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

DATABASE_URL = os.environ['DATABASE_URL']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL	

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
    post_data = Post.query.all()
    return render_template("blog.html", post_data = post_data)
    
@app.route("/img")
def img():
    return('''
    <a href="/">Home | </a>
    <a href="/img">Photos | </a>
    <a href="/blog">Blog</a>
    <h1>Personal site of M Wong</h1>
    <h2>Photos</h2>
    <h3>Australian Catholic University, Strathfield campus</h3>
    <img src="/static/acu4_flask.jpg">
    <br><br>

    <h3>UTS Haymarket Building 5, University of Technology Sydney</h3>
    <img src="/static/uts-bldg5.jpg">
    <br><br>
    ''')  

# access blog in local Windows PC
@app.route("/localblog")
def localblog():
    DATABASE = 'db1' # db1 is database file in local PC
    con = sqlite3.connect(DATABASE)
    #con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from tb1 order by id desc")
    rows = cur.fetchall()  
    return render_template("localblog.html", rows=rows)    
    
if __name__=="__main__":
    app.run()
 