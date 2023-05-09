from flask import *
from models import *
from database import init_db, db_session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Bingo1598'


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/ambassador/info")
def ambassador_info():
    return render_template("Aminfo.html")

@app.route("/privacy/policy")
def ambassador_info():
    return render_template("privacyPolicy.html")

@app.route("/ambassador/login", methods = ["GET", "POST"])
def ambassador_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        ambassador = db_session().query(Ambassador).where(Ambassador.email == email and Ambassador.password == password)
        if(ambassador == None):
            print("ambassador does not exist")
            #handle error here
        else:
            print("Ambassador logged in")  
            return render_template("home.html")
    else:
        return render_template("Amlogin.html")

@app.route("/ambassador")
def ambassador_loggedin():
    return render_template("Amloggedin.html")

@app.route("/apply", methods = ["GET", "POST"])
def ambassador_apply():
    if request.method == "POST":
        verify = False
        fname = request.form["firstName"]
        lname = request.form["lastName"]
        programs = request.form["socialPrograms"]
        gender = request.form["gender"]
        school = request.form["school"]
        email = request.form["email"]
        sa1 = request.form["SA1"]
        sa2 = request.form["SA2"]
        sa3 = request.form["SA3"]
        password = request.form["password"]
        confirm_password = request.form["confirmPassword"]
        # verify_password = db_session().query(Ambassador).where(Ambassador.password == password)
        if(password == confirm_password):
            verify = True
            print("password is good")
        # elif(verify_password != None):
        #     #handle error
        #     print("Password is taken")
        #     pass
        else:
            verify = False
            print("wrong password")
        if(verify):
            new_application = Application(fname, lname, gender, email, school, programs, sa1, sa2, sa3, password)
            #algorithm that sorts ambassador application into ambassadors
            is_ambassador = db_session().query(Ambassador).where(Ambassador.first_name == fname and Ambassador.last_name == lname and Ambassador.email == email and Ambassador.school == school)
            #if(is_ambassador == None):
            new_ambassador = Ambassador(email, password)
            Ambassador.application.append(new_application)
            Application.ambassadors.append(new_ambassador)
            db_session.add(new_ambassador)
            print("ambassador made")
            #else:
                #handle error
                #print("Ambassador already exists")
            db_session.add(new_application)
            db_session.commit()
            print("application made")
        return render_template("home.html")
    
    else:
        return render_template("Amapply.html")

@app.route("/newsletter/signup", methods = ["GET", "POST"])
def newsletter_signup():
    if request.method == "POST":
        email = request.form["email"]
        new_newsletter = Newsletter(email)
        db_session.add(new_newsletter)
        db_session.commit()
        print("newsletter made")
        return render_template("home.html")
    else:
        return render_template("newsletterSignUp.html")
    
    
    

@app.route("/about/the/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    init_db()
    app.run(debug = True)
