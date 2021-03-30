from app import db
# class Restaurants(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(50))
#     logo = db.Column(db.String(50))
class FAQ(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    question = db.Column(db.String(150))
    answer = db.Column(db.String(250))