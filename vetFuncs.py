from animalGenerator import generateobjects
import json

def readjsonfiles():
    ownerFile = open("ownerData.json","r")
    petFile = open("petData.json","r")
    listOfOwnerInfo = json.load(ownerFile)
    listOfPetInfo = json.load(petFile)
    return listOfOwnerInfo, listOfPetInfo

def storepetinfo(petData):
    file = open("petData.json","w")
    json.dump(petData,file)
    file.close()


def storeownerinfo(ownerData):
    file = open("ownerData.json","w")
    json.dump(ownerData,file)
    file.close()
    

def findownerbyid(ownerId):
    ownerInfo = []
    ownerData,petData = readjsonfiles()
    for owner in ownerData:
        if ownerId == owner.get("id"):
            ownerInfo.append(owner)
    if ownerInfo == []:
        ownerInfo.append("No Customer With This ID could be found")
    return ownerInfo

def findownerbypetid(petId):
    ownerInfo = []
    ownerData,petData = readjsonfiles()
    for pet in petData:
        if petId == pet.get("id"):
            ownerId = pet.get("ownerId")
            for owner in ownerData:
                if ownerId == owner.get("id"):
                    ownerInfo.append(owner)
    if ownerInfo == []:
        ownerInfo.append("No Customer Could be Found that Owns this pet") 
    return ownerInfo

def findpetbyid(petId):
    petInfo = []
    ownerData,petData = readjsonfiles()
    for pet in petData:
        if petId == pet.get("id"):
            petInfo.append(pet)
    if petInfo == []:
        petInfo.append("No Pets with this ID could be found")
    return petInfo

def findpetbyownerid(ownerId):
    petsInfo = []
    petIds = []
    ownerData,petData = readjsonfiles()
    for owner in ownerData:
        if ownerId == owner.get("id"):
            petIds.extend(owner.get("petIds"))
            for id in petIds:
                for pet in petData:
                    if id == pet.get("id"):
                        petsInfo.append(pet)
    if petsInfo == []:
        petsInfo.append("No Pets could be found that belong to the Owner with this ID")
    return petsInfo

def findpetbyname(petName):
    petsInfo = []   
    ownerData,petData = readjsonfiles()
    for pet in petData:
        if petName.lower() == pet.get("name").lower():
            petsInfo.append(pet)
    if petsInfo == []:
        petsInfo.append("No Pets could be found with that name")
    return petsInfo

def findownerbyname(ownerName):
    ownersInfo = []
    ownerData,petData = readjsonfiles()
    for owner in ownerData:
        if ownerName.lower() == owner.get("name").lower():
            ownersInfo.append(owner)
    if ownersInfo == []:
        ownersInfo.append("No Customers Could be found with that name")
    return ownersInfo