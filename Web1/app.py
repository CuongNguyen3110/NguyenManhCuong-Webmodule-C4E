from flask import Flask, render_template

app = Flask(__name__)

# function binding
@app.route("/")
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello C4E, hihi, haha"

@app.route("/me")
def me():
    return "Nguyen Manh Cuong"

@app.route("/hi/<name>")
def hi_name(name):
    return "Hi " + name

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    s = a + b
    return str(s)

@app.route("/posts/<int:index>")
def posts(index):
    titles = [
        "Trời mưa to quá",
        "Trời nắng to quá",
        "Trời nhiều mây"
    ]
    t = titles[index]
    contents = [
        "Tôi đi ra rồi lại đi vào",
        "Tôi đi đòi nợ, về tay không",
        "Toi o nha ngu"
    ]
    c = contents[index]
    return render_template("post.html", title=t, content=c)

@app.route("/movie")
def movie():
    return render_template("movie.html", name="Deadpool", image="https://www.dccomics.com/sites/default/files/GalleryChar_1920x1080_BM_Cv38_54b5d0d1ada864.04916624.jpg")

@app.route("/movies")
def movies():
    # movie_titles = [
    #     "Deadpool",
    #     "Black widow",
    #     "Iron man",
    #     "Clinkz"
    # ]
    movie_list = [
        {
            "title": "Deadpool",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Deadpool_%282016_poster%29.png/220px-Deadpool_%282016_poster%29.png"
        },
        {
            "title": "Batman",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/Darkknight_cd.jpg/220px-Darkknight_cd.jpg"
        },
        {
            "title": "Clinkz",
            "image": "https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/c/cb/Clinkz_icon.png"
        }
    ]
    return render_template("movies.html", movies=movie_list)
if __name__ == "__main__":
    app.run(debug=True)