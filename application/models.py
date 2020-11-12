from application import db 

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    reviews = db.relationship('Review', backref='series')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
