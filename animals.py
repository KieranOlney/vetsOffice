from abc import ABC, abstractmethod

class animal(ABC):
    #Attributes
    
    age = None
    name = None
    isAlive = True

    #Contructors

    def __init__(self,age,name):
        self.age = age
        self.name = name
    
    #Methods

    def die(self):
        self.isAlive = False
        return

    @abstractmethod
    def respire(self):
        pass

    @abstractmethod
    def eat(self):
        pass
    
    
    def sleep(self):
        sleeping = "I am Sleeping"
        return sleeping
    
    @abstractmethod
    def reproduce(self):
        pass

    
    def defocate(self):
        pooping = "I am Defocating"
        return pooping

    @abstractmethod
    def move(self):
        pass
   
    def grow(self):
        growing = "I am Growing"
        return growing

class mammal(animal):
    #Attributes

    #Contructors

    #Methods
    def move(self):
        moving = "I Am Walking"
        return moving

    @abstractmethod
    def eat(self):
        pass
    
    def respire(self):
        breathing = "I am Breathing"
        return breathing
    
    def reproduce(self):
        reproducing = "I am giving Birth"
        return reproducing

class bird(animal):
    #Attributes

    #Contructors

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

class cat(mammal):
    #Attributes

    #Contructors

    #Methods    
    def eat(self):
        eating = "I Eat Mice"
        return eating

class dog(mammal):
    #Attributes

    #Contructors

    #Methods
    def eat(self):
        eating = "I Eat bones and meat"
        return eating

class pidgeon(bird):
    #Attributes

    #Contructors

    #Methods
    def eat(self):
        eating = "I Eat people's leftovers"
        return eating

class parrot(bird):
    #Attributes

    #Contructors

    #Methods
    def eat(self):
        eating = "I Eat Worms"
        return eating