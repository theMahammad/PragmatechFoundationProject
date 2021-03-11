from flask import Flask,render_template,request,redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def addUser():
    return render_template("new.html")
@app.route("/users")
def showUsers():
    return render_template("users.html")
if __name__=="__main__":
    app.run(debug=True)
