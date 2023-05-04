from flask import *
from models import *
from database import init_db, db_session
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ambassador/info")
def ambassador_info():
    return render_template("Aminfo.html")

@app.route("/ambassador/login", methods = ["GET", "POST"])
def ambassador_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        ambassador = db_session().query(Ambassador).where(Ambassador.email == email and Ambassador.password == password)
        if(ambassador == None):
            print("ambassador does not exist")
        else:
            print("Ambassador logged in")
            pass
            #print a view with an error
        return redirect(url_for("ambassador_loggedin"))
    else:
        return render_template("Amlogin.html")

@app.route("/ambassador")
def ambassador_loggedin():
    return render_template("Amloggedin.html")

@app.route("/apply", methods = ["GET", "POST"])
def ambassador_apply():
    return render_template("Amapply.html")

@app.route("/newsletter/signup", methods = ["GET", "POST"])
def newsletter_signup():
    if request.method == "POST":
        email = request.form["email"]
        ambassador = db_session().query(Ambassador).where(Ambassador.email == email)
        is_ambassador = True
        if(ambassador == None):
            is_ambassador = False
        new_newsletter = Newsletter(is_ambassador, email)
        return redirect(url_for("home"))
    else:
        return render_template("newsletterSignUp.html")
    
    
    

@app.route("/about/the/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    init_db()
    app.run(debug = True)
