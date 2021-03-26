from flask import Flask 
from flask_pymongo import PyMongo

# config mongodb
app = Flask(__name__)
# app.secret_key = ""
app.config["MONGO_URI"] = "mongodb://localhost:27017/crud"
mongo = PyMongo(app)