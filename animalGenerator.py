from cat import cat
from dog import dog
from parrot import parrot
from pidgeon import pidgeon
from customer import customer
import flask  
from flask import request, jsonify
import json
import random

def generateobjects():
    cookie = cat(7,1,"Cookie")
    reggie = dog(3,2,"Reggie")
    chuck = parrot(2,3,"Chuck")
    ben = dog(8,4,"Ben")
    sooty = cat(12,5,"Sooty")
    tweetie = parrot(4,6,"Tweetie")
    kieran = customer(1,"Kieran")
    kieran.obtainPet(cookie)
    kieran.obtainPet(sooty)
    gareth = customer(2,"Gareth")
    gareth.obtainPet(reggie)
    gareth.obtainPet(tweetie)
    connor = customer(3,"Connor")
    connor.obtainPet(chuck)
    matt = customer(4,"Matt")
    matt.obtainPet(ben)

    owners = []
    pets = []
    owners.append(kieran)
    owners.append(gareth)
    owners.append(connor)
    owners.append(matt)
    pets.append(cookie)
    pets.append(reggie)
    pets.append(chuck)
    pets.append(ben)
    pets.append(sooty)
    pets.append(tweetie)
    ownersData = []
    petsData = []
    for owner in owners:
        ownersData.append(owner.dictOfAttributes())
    for pet in pets :
        petsData.append(pet.dictOfAttributes())
    return ownersData, petsData