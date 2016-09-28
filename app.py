from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('base.html')

#@app.route("/hello")
#def hello_world():
#    return render_template('hello_world.html')

@app.route("/hello/<name>")
def hello_person(name):
  return render_template('hello.html', name=name)
    
@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
  return render_template('jedi.html', first_name = first_name, last_name = last_name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
