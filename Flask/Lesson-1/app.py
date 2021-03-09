from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Salam avarelere</h1>"
@app.route("/update/<string:id>")
def updateAccordId(id):
  return f'The post whose id is {id} is updating'   

if __name__=="__main__":
    app.run(debug= True)