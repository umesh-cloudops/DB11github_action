from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "This is your app version 5 "

app.run(host='0.0.0.0', port=5000)
