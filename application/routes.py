from flask import render_template, redirect, url_for, request

from application import app,db

from application.models import Series, Review




@app.route('/home', methods = ['POST', 'GET'])
def index():
    render_template('')
