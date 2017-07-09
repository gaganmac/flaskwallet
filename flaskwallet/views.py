# views.py

from flask import render_template

from flaskwallet import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")