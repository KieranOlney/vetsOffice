from abc import ABC, abstractmethod
import datetime

class animal(ABC):
    #Attributes
    
    age = None
    name = None
    isAlive = True
    id = None
    ownerId = None
    LastVisitDate = None
    LastVisitedFor = None

    #Contructors

    def __init__(self,age,id,name):
        self.age = age
        self.id = id
        self.name = name
    
    #Methods
    
    def setname(self,name):
        self.name = name
        return True

    def die(self):
        self.isAlive = False
        return
    
    def sleep(self):
        sleeping = "I am Sleeping"
        return sleeping
    
    def defocate(self):
        pooping = "I am Defocating"
        return pooping
   
    def grow(self):
        growing = "I am Growing"
        return growing

    def visitVet(self,owner,reason):
        visitDate = datetime.datetime.now()
        owner.LastVisitDate = visitDate
        self.LastVisitDate = visitDate
        owner.LastVisitedFor = reason
        self.LastVisitedFor = reason
        return

    def dictOfAttributes(self):
        attributes = dict([("id",self.id),("name",self.name),("ownerId",self.ownerId),("age",self.age),("isAlive",self.isAlive),("lastVisitDate",self.LastVisitDate),("lastVisitedFor",self.LastVisitedFor)])
        return attributes