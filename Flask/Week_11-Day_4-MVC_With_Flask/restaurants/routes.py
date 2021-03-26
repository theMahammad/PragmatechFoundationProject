from app import app
@app.route("/restaurants")
def restaurant():
    return "It's the restaurant page"
    