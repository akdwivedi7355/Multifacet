from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return "Hello this is python deployed project on github"

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')

