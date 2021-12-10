from flask.wrappers import Request
import redis
from flask import Flask, request, jsonify
from classify import adder
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


with open('frontend.html') as f:
    frontend_template = f.read()

def prepare_frontend_template():
    return frontend_template

@app.route('/')
def hello():
    return '''
                <h1>Hello world</h1>
                <a> Enter your phrase to analyse</a>
                <input type="text" id="text_id" placeholder="text">
                <button type="button" onclick="analyse()"> Analyse </button>
                <br><a id="toChange"> Test </a>
                <script>

                function analyse() {
                    var inputmessage = document.getElementById("text_id").value
                    var response = fetch('http://localhost:5000/classify?inputmessage='+inputmessage)
                    .then((response) => response.json())
                    .then((json) => {
                        console.log(json)
                        document.getElementById("toChange").innerHTML = json
                    })
                }
                
                </script>'''


@app.route('/classify', methods=['GET'])
def classify():
    inputmessage = request.args.get('inputmessage')
    return jsonify("you entered {} ".format(inputmessage))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
