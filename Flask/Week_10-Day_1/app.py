from flask import Flask,render_template


app = Flask(__name__)
courses = [
    {
        'id' : 1,
        'title' : "Java Kursu",
        'desc' : "Java SE və Java EE birlikdə öyrənəcəksiniz",
        'img' : "../static/img/java.png"
    },
    {
        'id' : 2,
        'title' : "Python kursu",
        'desc' : "Pythonun hər şeyini öyrənəcəksiniz",
        'img' : "../static/img/python.png"
    },
    {
        'id' : 3,
        'title' : "Php kursu",
        'desc' : "Php barədə  hər şeyi öyrənəcəksiniz",
        'img' : "../static/img/php.png"
    },
    {
        'id' : 4,
        'title' : "Javascript kursu",
        'desc' : "Javascript barədə  hər şeyi öyrənəcəksiniz",
        'img' : "../static/img/js.png"
    }
    
]

@app.route("/")
def index():
    return render_template("index.html",courses = courses)

if __name__ == '__main__':
    app.run(debug=True)

