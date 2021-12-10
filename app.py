from flask import Flask
app = Flask(__name__)


with open('frontend.html') as f:
    frontend_template = f.read()

@app.route('/')
def hello():

    return frontend_template