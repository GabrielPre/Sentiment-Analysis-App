from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():

    return  '''
                <h1>Hello world</h1>
                <a> Enter your phrase to analyse</a>
                <input type="text" id="text_id" placeholder="text">
                <button type="button" onclick="analyse()"> Analyse </button>
                
                <script> 
                function analyse() {
                    var x = document.getElementById("text_id").value;
                    alert("You have entered "+x);
                }
                </script>'''