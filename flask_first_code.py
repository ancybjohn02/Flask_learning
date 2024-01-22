from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    # return 'Hello! first main page using flask <h1>Heyy<h1>'
    return 'The Biggest adventure you can ever take is to live the life of your dreams.<h1>Zeal<h1>'

@app.route('/<name>')
def user(name):
    return f"Hello {name}!"
if __name__ == "__main__":
    app.run()
