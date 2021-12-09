import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)


@app.route('/')
def hello():

    return '''
              <h1>Hello world</h1>
              <a> Enter your phrase to analyse</a>
              <input placeholder="">
              <button type="button"> Analyse </button>'''