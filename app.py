from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "This is your app Version 9 "

app.run(host='0.0.0.0', port=5000)
