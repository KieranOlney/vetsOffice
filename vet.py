from cat import cat
from dog import dog
from parrot import parrot
from pidgeon import pidgeon
from customer import customer
from animalGenerator import generateobjects
import flask  
from flask import render_template, request, jsonify
from vetFuncs import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def home():

    return "<h1>Welcome to Kieran's API work</h1>"

@app.route("/api/customers", methods=["GET"])
def getCustomerInfo():
    if 'ownerId' in request.args:
        id = int(request.args['ownerId'])
    else:
        return "Error: No Owner with that Id Found"
    ownerInfo = findOwnerById(id)
    return jsonify(ownerInfo)

@app.route("/api/customers/all", methods=["GET"])
def getAllCustomers():
    ownerInfo, petInfo = readJSONFiles()
    return jsonify(ownerInfo)

@app.route("/api/pets", methods=["GET"])
def getPetInfo():
    if 'petId' in request.args:
        id = int(request.args['petId'])
    else:
        return "Error: No Pet with that Id Found"
    petInfo = findPetById(id)
    return jsonify(petInfo)

@app.route("/api/pets/all", methods=["GET"])
def getAllPets():
    ownerInfo, petInfo = readJSONFiles()
    return jsonify(petInfo)

app.run()