from flask import Flask

#main variable to use
app = Flask(__name__)

#start creating the endpoints 

@app.route("/")
def hello():
    return "Hello,there!"

@app.route("/ping")
def xyz():
    return "message : Why are you pinging me?"