from flask import Flask,render_template,request,redirect
app = Flask(__name__)
kitablar = []
id=1
class Kitab():
    """
    id
    ad
    yazar_adi
    qiymet

    """
    def __init__(self,id,ad,yazar_adi,qiymet):
        self.id=id
        self.ad=ad
        self.yazar_adi=yazar_adi
        self.qiymet=qiymet

@app.route("/" , methods=['GET','POST'])
def index():

    global id
    if len(kitablar)==0:
        id=1

    if request.method=="POST":
        kitab = Kitab(
            id = id, 
            ad=request.form['kitab_adi'],
            yazar_adi=request.form['yazar_adi'],
            qiymet=int(request.form['kitab_qiymeti'])
            )
        kitablar.append(kitab)
        id+=1
        return redirect("/")
    return render_template("index.html",books = kitablar)
@app.route("/update/<int:id>" ,methods=['GET','POST'])
def updateKitab(id):
    sechilmisKitab = None
    for kitab in kitablar:
        if kitab.id==id:
            sechilmisKitab=kitab
    if request.method=="POST":
        sechilmisKitab.ad=request.form['kitab_adi']
        sechilmisKitab.yazar_adi=request.form['yazar_adi']
        sechilmisKitab.qiymet=int(request.form['kitab_qiymeti'])
        return redirect("/")
    return render_template("update.html",sechilmisKitab = sechilmisKitab)
@app.route("/delete/<int:id>")
def deleteKitab(id):
    for kitab in kitablar:
        if kitab.id==id:
            kitablar.remove(kitab)
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)