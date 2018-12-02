import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from nltk.tag import pos_tag
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('URI', 'Optional default value'))
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv('DB_NAME', 'Optional default value')
app.config["MONGO_URI"] = os.getenv('URI', 'Optional default value')



mongo = PyMongo(app)


@app.route("/")
def find_recipe():
    recipe = mongo.db.recipes.find_one()
    return render_template("recipes.html", recipe=recipe)


@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html")

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            
