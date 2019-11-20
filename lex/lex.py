from flask import Flask,render_template
import os

app = Flask(__name__)

app.static_folder = 'templates'
environment=os.getenv("ENVIRONMENT","development")

@app.route("/")
def index():
    return  render_template('index.html')

@app.route("/lex")
def lex():
    return "hola lex"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    debug=False
    if environment == "development" or environment == "local":
        debug=True