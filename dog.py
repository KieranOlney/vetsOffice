from mammal import mammal

class dog(mammal):
    #Attributes

    #Contructors
    def __init__ (self,age,id,name):
        super().__init__(age,id,name)

    #Methods
    def eat(self):
        eating = "I Eat bones and meat"
        return eating