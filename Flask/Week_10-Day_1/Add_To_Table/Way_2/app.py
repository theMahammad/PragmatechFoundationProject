from flask import Flask,render_template,request,redirect
user_list = [] 
id =0
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/users",methods = ["GET","POST"])
def users():
    global id
    if request.method =="POST":
        id+=1
        name = request.form.get("name")
        surname = request.form.get("surname")
        user_list.append(
            {   'id'   : id,
                'name' : name,
                'surname':surname
            }
        )
        return render_template("users.html",id = id, user_list = user_list)
    else:
        return render_template("users.html")
@app.route("/delete/<int:ide>")
def delete(ide):
    for user in user_list:
        if(user['id']) == ide:
            user_list.remove(user)
            return redirect("/users")
       
    return render_template("users.html",user_list= user_list)
if __name__=='__main__':
    app.run(debug=True)