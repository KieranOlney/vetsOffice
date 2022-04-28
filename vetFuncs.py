from importlib.metadata import PackageMetadata
from animalGenerator import generateobjects
import json

def readJSONFiles():
    ownerFile = open("ownerData.json","r")
    petFile = open("petData.json","r")
    listOfOwnerInfo = json.load(ownerFile)
    listOfPetInfo = json.load(petFile)
    return listOfOwnerInfo, listOfPetInfo

def storePetInfo(petData):
    file = open("petData.json","w")
    json.dump(petData,file)
    file.close()
    return

def storeOwnerInfo(ownerData):
    file = open("ownerData.json","w")
    json.dump(ownerData,file)
    file.close()
    return

def findOwnerById(ownerId):
    ownerInfo = []
    ownerData,petData = readJSONFiles()
    for owner in ownerData:
        if ownerId == owner.get("id"):
            ownerInfo = owner
    return ownerInfo

def findOwnerByPetId(petId):
    ownerData,petData = readJSONFiles()

    return ownerInfo

def findPetById(petId):
    ownerData,petData = readJSONFiles()

    return petInfo

def findPetsByOwnerId(ownerId):
    ownerData,petData = readJSONFiles()

    return petsInfo

