
from datetime import datetime
from flask import render_template
from python_webapp_flask import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About'
    )