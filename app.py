import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from nltk.tag import pos_tag
from pprint import pprint


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "test-cookbook"
app.config["MONGO_URI"] = "mongodb://admin:kawaii1010@ds155823.mlab.com:55823/test-cookbook"

mongo = PyMongo(app)


@app.route("/")
def find_recipe():
    return render_template("recipes.html")


@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html")

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
