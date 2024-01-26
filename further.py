from flask import Flask,redirect, url_for,render_template
app = Flask(__name__)
a = False

@app.route('/<name>')
def home(name):
    # return 'Hello! first main page using flask <h1>Heyy</h1>'
   return render_template("index1.html",content =name)

 

# you can pass in more like this content here with diff variabke name 
# and just making a new line of <p> {{wraf}} </p> and giving it's value near content as wraf =__

@app.route('/<name>')
def user(name):
    return f"Heyy {name}!"

@app.route("/admin")
def admin():
    if a:
        return redirect(url_for("home", name = "hehe!"))



if __name__ == "__main__":
    app.run()
