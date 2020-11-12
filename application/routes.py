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

@app.route('/update/<int:idNum>', methods=['GET', 'POST'])
def update(idNum):
    form = SeriesForm()
    series_update = Series.query.get(idNum)
    if form.validate_on_submit():
        series_update.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)


@app.route('/delete/<int:idNum>')
def delete(idNum):
    series_delete = Series.query.get(idNum)
    db.session.delete(series_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addReview/<int:idNum>', methods=['GET', 'Post'])
def addReview(idNum):
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(desc=form.desc.data,
			rating=form.rating.data,
			series_id=idNum)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('Reviewpage', idNum=idNum))
    return render_template('addReview.html', form=form, series = Series.query.get(idNum))

@app.route('/Reviewpage/<int:idNum>', methods=['GET','POST'])
def Reviewpage(idNum):
    review_page = Review.query.filter_by(series_id=idNum).all()
    return render_template('Reviewpage.html', review_page=review_page)

