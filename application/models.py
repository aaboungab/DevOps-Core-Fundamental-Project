from application import db 

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    seasons = db.Column(db.Integer, nullable=False)

class Review(db.Model):
    reviewid = db.Column(db.Integer, primary_key=True, nullable=False)
    descrp = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Integer(5), nullable=False)
    seriesid = db.Column(db.Integer, db.ForeignKey('Series.id'), nullable=False)
