from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def name(username):
    user_list = {
        "Cuong": {
            "name": "Nguyen Manh Cuong",
            "gender": "Nam",
            "age": 23
        },
        "Luong": {
            "name": "Le Thi Luong",
            "gender": "Nu",
            "age": 23
        }
    }
    if username in user_list.keys():
        a = user_list[username]
        return render_template("user.html", name=a["name"], gender=a["gender"], age=a["age"])
    else:
        return "user not found"

if __name__ == "__main__":
    app.run(debug=True)