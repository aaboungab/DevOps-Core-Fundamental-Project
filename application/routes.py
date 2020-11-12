from flask import render_template, redirect, url_for, request

from application import app, db
from application.forms import SeriesForm, ReviewForm
from application.models import Series, Review


@app.route('/', methods = ['POST', 'GET'])
def index():
    all_series = Series.query.all()
    return render_template('index.html', all_series=all_series)

@app.route('/addSeries', methods = ['GET', 'POST'])
def add():
    form = SeriesForm()
    if form.validate_on_submit():
        new_series = Series(name=form.name.data)
        db.session.add(new_series)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addSeries.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = SeriesForm()
    series_update = Series.query.get(id)
    if form.validate_on_submit():
        series_update.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)


@app.route('/delete/<int:id>')
def delete(id):
    series_delete = Series.query.get(id)
    db.session.delete(series_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addReview/<int:id>', methods=['GET', 'Post'])
def addReview(id):
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(desc=form.desc.data,
			rating=form.rating.data,
			series_id=id)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('Reviewpage', id=id))
    return render_template('addReview.html', form=form, series = Series.query.get(id))

@app.route('/Reviewpage/<int:id>', methods=['GET','POST'])
def Reviewpage(id):
    review_page = Review.query.filter_by(series_id=id).all()
    return render_template('Reviewpage.html', review_page=review_page)
     
