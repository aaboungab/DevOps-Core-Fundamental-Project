from application import db 

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    revs = db.relationship('Review', backref='series')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(30), unique=True )
    rating = db.Column(db.Integer)
    seriesid = db.Column(db.Integer, db.ForeignKey('series.id'))
