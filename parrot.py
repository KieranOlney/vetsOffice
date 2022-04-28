from bird import bird

class parrot(bird):
    #Attributes

    #Contructors
    def __init__ (self,age,id,name):
        self.type = "Parrot"
        super().__init__(age,id,name)

    #Methods
    def eat(self):
        eating = "I Eat Worms"
        return eating