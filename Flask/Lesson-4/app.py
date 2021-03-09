from flask import Flask,render_template,request
app = Flask(__name__)
user = []

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/user-list",methods = ["GET","POST"])

def userList():
   
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        fullname = name+" "+surname
        user.append(fullname)
        
       
        return render_template("list.html",user_list = user)
    else:
        
        return render_template("list.html")



if __name__ == "__main__":
    app.run(debug=True)
