from flask import Flask, redirect, render_template

web = Flask(__name__)

@web.route("/about-me")
def about_me():
    me = {
        "name": "Nguyen Manh Cuong",
        "Age": 23,
        "school": "Techkids"
    }
    return render_template("about_me.html", name=me["name"], age=me["age"], school=me["school"])

@web.route("/school")
def school():
    return redirect("http://techkids.vn", code=302)


if __name__ == "__main__":
    web.run(debug=True)
