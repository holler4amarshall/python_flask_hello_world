# python_flask_hello_world
a brief demo of a web application using python and flask

# How to run the app

* Access the web application's [index page](https://stark-savannah-98416.herokuapp.com)
  * Here, you can see the information served from the base jinja template
* Manually add '/hello' to the URL to access https://stark-savannah-98416.herokuapp.com/hello
  * Here, you can see the information served from the 'base' jinja template, along with the information from the 'hello_world' jinja template
* Manually add '/hello/your_first_name' to the URL to access https://stark-savannah-98416.herokuapp.com/hello/holly
  * Here, you can see the information served from the 'base' jinja template, along with the information from the 'hello' jinja template
* Manually add '/jedi/your_first_name/your_last_name' to the URL to access https://stark-savannah-98416.herokuapp.com/jedi/holly/copter
  * Here, you can see the information served from the 'base' jinnja template, along with the information from the 'jedi' jinja template
  * The jedi template also uses jinja filters in order to display template variables according to requirements

# Project information

This project was created in order to develop skills in Python, Flask, Jinja and Heroku. 

*The 1st commit of the project demonstrates using Flask to build a simple web application*
After creating a python virtual environment, the project was built using a Flask virtual environment. 
Functions and Decorators (such as @app.route) were used in order to tell Flask what action to perform when a URL path is visited. When a function returns a string, Flask interprets the code as HTML. This demonstration shows how Flask can handle creating very simple web applications. 

*The 2nd commit of the project demonstrates using Jinja templates with Flask & Python*
Functionality specific to each web page was separated into Jinja templates. Common code (such as footers) was placed in the base jinja template. An 'app.py' file was created in order to pull the project together, by making use of the Flask decorators to instruct the program what to do when a particular URL is accessed. The associated functions then referred to the Jinja templates. 

*The final commits of the project demonstrate using Heroku to host the web application*
The web application project was finally deployed to a Heroku virtual machine (dynos) so that it can be accessible via the URL: https://stark-savannah-98416.herokuapp.com

Note that the project uses very simple HTML and is not overly user friendly! The purpose of the project was to learn about basic Flask, Jinja and Heroku functions. 
