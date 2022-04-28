from bird import bird

class pidgeon(bird):
    #Attributes

    #Contructors
    def __init__ (self,age,id,name):
        super().__init__(age,id,name)

    #Methods
    def eat(self):
        eating = "I Eat Ciggie Butts"
        return eating