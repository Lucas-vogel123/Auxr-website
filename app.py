from flask import *
from models import *
from database import init_db, db_session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Bingo1598'

#takes you to ambassador info page
@app.route("/ambassador/info")
def ambassador_info():
    return render_template("Aminfo.html")


#takes you to our homepage
@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

#privacy policy linked through footer
@app.route("/privacy/policy")
def privacy_policy():
    return render_template("privacyPolicy.html")

#ambassador login page
@app.route("/ambassador/login", methods = ["GET", "POST"])
def ambassador_login():
    #if you get a post request
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        ambassador = db_session().query(Ambassador).where((Ambassador.email == email) & (Ambassador.password == password)).first()
        #checks if the person logging in is an ambassador
        if(ambassador == None):
            #show an error message if they arent
            flash("ambassador does not exist")
            return redirect(url_for("ambassador_login"))
        else:
            print("Ambassador logged in")  
            return redirect(url_for("homepage"))
    else:
        return render_template("Amlogin.html")

@app.route("/ambassador")
def ambassador_loggedin():
    return render_template("Amloggedin.html")

@app.route("/apply", methods = ["GET", "POST"])
def ambassador_apply():
    if request.method == "POST":
        #gathers all the information in the application
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
        verify_password = db_session().query(Ambassador).where(Ambassador.email == email)
        #checks if passwords are matching
        if(password == confirm_password):
            verify = True
            print("email is good")
        elif(verify_password != None):
            #handles error
            flash("email is already registered")
        else:
            verify = False
            print("wrong password")
        if(verify):
            new_application = Application(fname, lname, gender, email, school, programs, sa1, sa2, sa3, password)
            #checks if they are already an ambassador
            is_ambassador = db_session().query(Ambassador).where((Ambassador.first_name == fname) & (Ambassador.last_name == lname) & (Ambassador.email == email)).first()
            if(is_ambassador == None):
                db_session.add(new_application)
                db_session.commit()
                new_ambassador = Ambassador(email, fname, lname, password)
                new_ambassador.application = [new_application]
                db_session.add(new_ambassador)
                print("ambassador made")
            else:
                #handles error if they are an ambasssador
                flash("Ambassador already exists")
                return redirect(url_for("ambassador_apply"))
            db_session.commit()
            print("application made")
        return redirect(url_for("homepage"))
    
    else:
        return render_template("Amapply.html")

@app.route("/newsletter/signup", methods = ["GET", "POST"])
def newsletter_signup():
    if request.method == "POST":
        #takes in an email and signs it up for newsletter
        email = request.form["email"]
        already_registered = db_session().query(Newsletter).where(email == Newsletter.email).first()
        if(already_registered == None):
            new_newsletter = Newsletter(email)
            db_session.add(new_newsletter)
            db_session.commit()
            print("newsletter made")
        else:
            flash("email is already regsitered")
            return redirect(url_for("newsletter_signup"))
        return redirect(url_for("homepage"))
    else:
        return render_template("newsletterSignUp.html")

@app.route("/about/the/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    init_db()
    app.run(debug = True)
