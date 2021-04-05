from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import TextAreaField

app = Flask(__name__)
app.config["SECRET_KEY"]="salam"

class TextForm(FlaskForm):
    text = TextAreaField('summernote')
@app.route("/",methods=  ["GET","POST"])
def index():
    form = TextForm()
    if request.method =="POST":
        data = form.text.data
    return render_template("index.html",data = form.text.data,form = form)

if __name__=="__main__":
    app.run(debug=True)