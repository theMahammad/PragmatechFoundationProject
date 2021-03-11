from flask import Flask,render_template,request
user_list = [] 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/users",methods = ["GET","POST"])
def users():
    if request.method =="POST":
       
        name = request.form.get("name")
        surname = request.form.get("surname")
        user_list.append(name+" "+surname)
        length = len(user_list)
        return render_template("users.html",length = length, user_list = user_list)
    else:
        return render_template("users.html")

if __name__=='__main__':
    app.run(debug=True)