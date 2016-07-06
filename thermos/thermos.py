from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, url_for, flash

app = Flask(__name__)

bookmarks = []
app.config["SECRET_KEY"] = "o\xde\x87&\xf9\xc7\x00hJ*\xe5\x94\xbd\xd3\xef\x8a\xa3D\xa3P\x8b\x1a:]"

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "gonz",
        date = datetime.utcnow()
    ))
def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm["date"], reverse=True)[:num]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", new_bookmarks = new_bookmarks(5))
        
@app.route("/add", methods=["GET", "POST"])
def add():
    if  request.method == "POST":
        url = request.form["url"]
        store_bookmark(url)
        flash("Stored bookmak '{}'".format(url))
        return redirect(url_for("index"))
    return render_template("add.html")
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
    
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
    
