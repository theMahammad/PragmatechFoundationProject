from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Drug(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    country = db.Column(db.String(50))
    company = db.Column(db.String(50))
    specifications = db.Column(db.String(250))
@app.route('/',methods=['GET','POST'])
def home():
    return render_template("index.html")

# ADD
@app.route('/add_drug', methods = ["GET","POST"])
def addDrug():
    if request.method=="POST":
        drug = Drug(
        name = request.form['drug-name'],
        country = request.form['drug-country'],
        company = request.form['drug-company'],
        specifications = request.form['drug-specifications']
        )
        db.session.add(drug)
        db.session.commit()
        return redirect('/drugs')
        
    return render_template("add_drug.html")

# UPDATE
@app.route("/update/<int:id>",methods = ["GET","POST"])
def updateDrug(id):
    currentDrug = Drug.query.get(id)
    if request.method=="POST":
        currentDrug.name  = request.form['drug-name']
        currentDrug.country = request.form['drug-country']
        currentDrug.company = request.form['drug-company']
        currentDrug.specifications = request.form['drug-specifications']
        db.session.commit()
        return redirect('/drugs')
    return render_template("update_drug.html",currentDrug = currentDrug)
# DELETE
@app.route('/delete/<int:id>')
def deleteDrug(id):
    db.session.delete(Drug.query.get(id))
    db.session.commit()
    return redirect("/drugs")

# SHOW
@app.route('/drugs')
def showDrugs():
    drugs = Drug.query.all() 
    return render_template("drugs.html",drugs = drugs)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)