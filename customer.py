import datetime

class customer():
    #Attributes

    #Contructors
    def __init__ (self,id,name):
        self.id = id
        self.name = name
        self.petIds = []
        self.LastVisitDate = None
        self.LastVisitedFor = None

    #Methods

    def obtainPet(self,pet):
        self.petIds.append(pet.id)
        pet.ownerId = self.id

    def renamePet(self,pet,desiredName):
        pet.name = desiredName
    
    def dictOfAttributes(self):
        attributes=dict([("id",self.id),("name",self.name),("petIds",self.petIds),("lastVisitDate",self.LastVisitDate),("lastVisitedFor",self.LastVisitedFor)])
        return attributes

