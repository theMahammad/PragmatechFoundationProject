from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def index():
    arr= ["Aylı","Gecə","Sərin","Külək"]
    return render_template("index.html",person = "Mehemmed Sadigzade",age = 17,arr = arr)

if __name__=="__main__":
    app.run(debug=True)