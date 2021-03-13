from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    details = db.Column(db.String(250))

@app.route('/')
def home():
      
    return render_template('index.html')
@app.route("/new",methods = ["GET","POST"])
def addUser():
    if request.method=="POST":
        _name = request.form.get("name")
        _surname= request.form.get("surname")
        _email = request.form.get("mail")
        _details = request.form.get("details")
        user = User(name = _name,surname = _surname,email = _email,details = _details)
        db.session.add(user)
        db.session.commit()
        return redirect("/users")
       
    return render_template("new.html")
@app.route("/users",methods = ["GET","POST"])
def showAllUser():
    allUsers = User.query.all()
    return render_template("users.html",allUsers = allUsers)
# Delete data from database
@app.route("/delete/<id>")
def delete(id):
    userForDelete = User.query.get(id)
    db.session.delete(userForDelete)
    db.session.commit()
    return redirect("/users") 
#See Details in user Profile
@app.route("/users/<int:id>")
def showDetails(id):
    userComprehensive = User.query.get(id)
    return render_template("detail.html",user = userComprehensive)
@app.route("/update/<int:id>",methods = ["GET","POST"])
def updateData(id):
    user=User.query.get(id)
    if request.method=="POST":
        user.name = request.form.get("name")
        user.surname= request.form.get("surname")
        user.email = request.form.get("mail")
        user.details = request.form.get("details")
        db.session.commit()
        return redirect("/users")
    return render_template("update.html",_user=user)
if __name__ == '__main__':
   app.run(debug=True)