from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

#@app.route("/hello/<name>")
#def hi_person(name):
#    return "Hello {}!".format(name.title())

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
    html = """
        <body background="http://www.medievalists.net/wp-content/uploads/2014/03/Kenobi-medieval-monk.jpg">
            <p>your jedi name is...</p>
            <h1>{}{}!</h1>
        </body>
    """
    return html.format(first_name[:3].capitalize(),last_name[:3].lower()).title()

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
