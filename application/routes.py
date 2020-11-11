from flask import render_template, redirect, url_for, request

from application import app, db
from application.forms import SeriesForm, ReviewForm
from application.models import Series, Review


@app.route('/', methods = ['POST', 'GET'])
def index():
    all_series = Series.query.all()
    return render_template('index.html', all_series=all_series)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = SeriesForm()
    if form.validate_on_submit():
        new_series = Series(name=form.name.data)
        db.session.add(new_series)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addSeries.html', form=form)

@app.route('/update/<int:series_id>', methods=['GET', 'POST'])
def update(series_id):
    form = SeriesForm()
    series_to_update = Series.query.get(series_id)
    if form.validate_on_submit():
        series_to_update.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)


@app.route('/delete/<int:series_id>')
def delete(series_id):
    series_to_delete = Series.query.get(series_id)
    db.session.delete(series_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addReview', methods=['GET', 'Post'])
def addReview():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(desc=form.desc.data)
        review_rating = Review(rating=form.rating.data)
        db.session.add(new_review)
        db.session.add(review_rating)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addReview.html', form=form)
