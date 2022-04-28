from animal import animal
from abc import ABC, abstractmethod

class bird(animal):
    #Attributes

    #Contructors
    def __init__ (self,age,id,name):
        super().__init__(age,id,name)

    #Methods      
    def move(self):
        moving = "I Am Flying/Walking"
        return moving

    @abstractmethod
    def eat(self):
        pass
    
    def respire(self):
        breathing = "I am Breathing"
        return breathing
    
    def reproduce(self):
        reproducing = "I am laying an egg"
        return reproducing