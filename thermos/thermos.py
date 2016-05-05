from flask import Flask, render_template, url_for
app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route("/")
@app.route("/index")
def hello():
    return render_template(
        'index.html',
        title="Title passed from view to template",
        user=User("Gonzalo", "Lucero"))

if __name__ == "__main__":
    app.run(debug=True)
    
