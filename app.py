from flask import Flask, request, jsonify
from vetFuncs import findOwnerById,findOwnerByName,findOwnerByPetId,findPetById,findPetByName,findPetsByOwnerId,readJSONFiles

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def home():

    return "<h1>Welcome to Kieran's API work</h1><a href='/api/customers/all'>Customer List</a><p></p><a href='/api/pets/all'>Pet List</a>"

@app.route("/api/customers", methods=["GET"])
def getcustomerinfo():
    if 'ownerId' in request.args:
        ownerid = int(request.args['ownerId'])
        ownerinfo = findOwnerById(ownerid)
    elif 'petId' in request.args:
        ownerid = int(request.args['petId'])
        ownerinfo = findOwnerByPetId(ownerid)
    elif 'ownerName' in request.args:
        ownername = str(request.args['ownerName'])
        ownerinfo = findOwnerByName(ownername)
    else:
        return "Error: No Recognised Argument Provided, This function's Argument should be 'ownerId' or 'petId"

    return jsonify(ownerinfo)

@app.route("/api/customers/all", methods=["GET"])
def getAllCustomers():
    ownerinfo, petinfo = readJSONFiles()
    return jsonify(ownerinfo)

@app.route("/api/pets", methods=["GET"])
def getpetinfo():
    if 'petId' in request.args:
        petid = int(request.args['petId'])
        petinfo = findPetById(petid)
    elif 'ownerId' in request.args:
        petid = int(request.args['ownerId'])
        petinfo = findPetsByOwnerId(petid)
    elif 'petName' in request.args:
        petname = str(request.args['petName'])
        petinfo = findPetByName(petname)
    else:
        return "Error: No Recognised Argument Provided, This function's Argument should be 'petId' or 'ownerId'"
    return jsonify(petinfo)

@app.route("/api/pets/all", methods=["GET"])
def getAllPets():
    ownerinfo, petinfo = readJSONFiles()
    return jsonify(petinfo)

if __name__ == "__main__":
    app.run()