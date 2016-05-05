from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
        
@app.route("/add")
def add():
    return render_template("add.html")
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
    
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
    
