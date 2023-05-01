from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("../templates/home.html")

@app.route("/ambassador_info")
def ambassador_info():
    return render_template("../templates/Aminfo.html")

@app.route("/ambassador_login")
def ambassador_login():
    return render_template("../templates/Amlogin.html")

@app.route("/ambassador")
def ambassador_loggedin():
    return render_template("../templates/Amloggedin.html")

@app.route("apply")
def ambassador_apply():
    return render_template("../templates/Amapply.html")

@app.route("newsletter_signup")
def newsletter_signup():
    return render_template("../templates/newsletterSign.html")

@app.route("about_the_team")
def team():
    return render_template("../templates/team.html")

if __name__ == "main":
    app.run()
