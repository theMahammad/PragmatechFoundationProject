from flask import Flask,redirect,url_for,render_template,request
from app import app
from restaurants import routes
@app.route("/")
def index():
    return "Salam avarelere"
if __name__ == '__main__':
    app.run(debug=True)