from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    personSurname = "Sadigzade"
    return render_template("index.html",personName= input("Kim döndü doğrudan?"),personSurname = "Sadigzade")


if __name__ =="__main__":
    app.run(debug=True)
