from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ambassador_info")
def ambassador_info():
    return render_template("Aminfo.html")

@app.route("/ambassador_login")
def ambassador_login():
    return render_template("Amlogin.html")

@app.route("/ambassador")
def ambassador_loggedin():
    return render_template("Amloggedin.html")

@app.route("/apply")
def ambassador_apply():
    return render_template("Amapply.html")

@app.route("/newsletter_signup")
def newsletter_signup():
    return render_template("newsletterSignUp.html")

@app.route("/about_the_team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug = True)
