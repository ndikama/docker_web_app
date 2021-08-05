# from flask import Flask

# app = Flask(name)


# @app.route('/')
# # route de base de l'application
# def hello():
#     return "Hello world"



from flask import Flask, request
from flask.templating import render_template
from model.continentModel import ContinentModel
from werkzeug.utils import redirect

app = Flask(__name__)

continent = ContinentModel()
URI = "localhost"

# @app.route("/")
# def hello():
#     return "hellow world"

@app.route('/')
def hello():
    result = continent.fetch_all_continent()
    return render_template("bonjour.html", data=result)


@app.route('/add_continent_template/')
def add_continent_template():
    return render_template("add_continent.html")


@app.route('/insert_continent', methods=['POST', 'GET'])
def insert_continent():
    data = request.form
    continent.add_continent(data)
    return redirect('http://127.0.0.1:5010')


@app.route('/delete_continent/<id>')
def delete_continent(id):
    continent.delete_continent(id)
    return redirect("/")


@app.route('/update_continent_template')
def update_continent_template():
    data = request.args
    return render_template("update_continent.html", data=[data])

@app.route('/update_continent', methods=['POST', 'GET'])
def update_continent():
    data = request.form
    continent.update_continent(data)
    return redirect('http://127.0.0.1:5010')