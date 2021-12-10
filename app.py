from flask import Flask, request
app = Flask(__name__)


with open('frontend.html') as f:
    frontend_template = f.read()

def prepare_frontend_template():
    return frontend_template

@app.route('/')
def hello():
    return prepare_frontend_template()