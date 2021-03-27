from app import db
class Restaurant(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    CEOES = db.relationship('restaurant',backref='restaurant',lazy=True)
class CEO(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    rest_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'))