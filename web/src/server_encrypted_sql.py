from flask import Flask, render_template, request
from sqlite_select import select
from sqlite_insert import insert
import hashlib

md5 = hashlib.md5()
salt = "randomstring"


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route("/signin", methods=["GET"])
def signin_form():
    return render_template("signin.html")

@app.route("/signin",methods=["POST"])
def signin():
    name = request.form["username"]
    passwd = request.form["password"]
    # if name in dict and dict[name]==passd:
    passwd = hashlib.md5((salt+passwd).encode('utf-8')).hexdigest()
    signal = select(name)
    if not(signal is None) and signal[0]==passwd:
        return render_template("signin_ok.html",message = "hello, %s" % name, username=name)
    return render_template("signin.html",message="bad username or password")

@app.route("/signup", methods=["GET"])
def signup_form():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["username"]
    passwd = request.form["password"]
    # if name in dict:
    if not (select(name) is None):
        return render_template("signin.html",username=name,message="%s exists, please sign in directly!" % name)
    passwd = hashlib.md5((salt+passwd).encode('utf-8')).hexdigest()
    insert(name,passwd)
    return render_template("signin.html",message="signup success,please signin",username=name)

if __name__ == '__main__':

    app.run()
