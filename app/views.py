#this file allows us to access views (html and other files)

from app import app

#import the render_template method
from flask import render_template

#first view (index)
@app.route("/")
def index():
    return render_template("public/index.html")

#second view (about)
@app.route("/about")
def about():
    return "<h1 style='color:red;'>I'm a red H1 heading!</h1>"
