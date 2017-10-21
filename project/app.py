from flask import Flask 
from flask import render_template

app = Flask(__name__) # create an instance of the Flask class for our web app

@app.route("/")
def index():
    #The method "render_template" will generate a jinja2 template object 
    #out of that HTML and return it to the browser when the user visits 
    #associated URL.
    return render_template("index.html") 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

