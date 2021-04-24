from flask import Flask, render_template, request

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
    passd = request.form["password"]
    if name in dict and dict[name]==passd:
        return render_template("signin_ok.html",message = "hello, %s" % name, username=name)
    return render_template("signin.html",message="bad username or password")

@app.route("/signup", methods=["GET"])
def signup_form():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["username"]
    passd = request.form["password"]
    if name in dict:
        return render_template("signin.html",username=name,message="%s exists, please sign in directly!" % name)
    dict[name] = passd
    return render_template("signin.html",message="signup success,please signin",username=name)


if __name__ == '__main__':
    # 创建一个虚拟数据库，存储用户名和密码
    dict = {"jhh":"123456"}
    app.run()
