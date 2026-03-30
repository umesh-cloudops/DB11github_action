from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "self hosted runner github_action  "

app.run(host='0.0.0.0', port=5000)
