import mlab
from class_register import Register
from flask import Flask, render_template, request
from gmail import GMail, Message

mlab.connect()

app = Flask(__name__)
gmail = GMail("cuongnguyen1.fit@gmail.com", "footballistaste")
content = "<p>Welcome</p>"
message = Message("Welcome", to="cuongnm3110@gmail.com", html=content)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        name = form["username"]
        pw = form["password"]
        exist_user = Register.objects(username=u).first()
        if exist_user != None:
            return "User already exists!"
        else:
            m = Register(username=name, password=pw)
            m.save()
            gmail.send(message)
            return "Gotcha!!"

if __name__ == "__main__":
    app.run(debug=True)

