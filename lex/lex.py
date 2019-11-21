from flask import Flask,render_template
import os

app = Flask(__name__)

app.static_folder = 'static'
app.template_folder= 'templates'
environment=os.getenv("ENVIRONMENT","development")
data = "hello flask"
@app.route("/")
def index():
    return  render_template('index.html', data=data)

@app.route("/lex")
def lex():
    return "hola lex"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    debug=True
    if environment == "development" or environment == "local":
        debug=True