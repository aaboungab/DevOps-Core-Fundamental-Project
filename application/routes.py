from flask import render_template, redirect, url_for, request

from application import app, db

from application.models import Series, Review


@app.route('/', methods = ['POST', 'GET'])
def index():
    all_reviews = Review.query.all()
    return render_template('index.html', all_reviews=all_reviews)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    new_review = Review(desc='New Review')
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for('index'))
