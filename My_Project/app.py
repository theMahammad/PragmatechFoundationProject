from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
db = SQLAlchemy(app)

@app.route("/")
def homePage():
    return render_template("app/home-page.html")
if __name__=="__main__":
    app.run(debug=True)
