class Chai:
    def __init__(self,sweetness,milk_level):
        self.sweetness=sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("Sipping chai")
    def addedSugars(self,amout):
        self.sweetness = self.sweetness + amout
        print(f"Added Sugars {self.sweetness} ")

my_chai= Chai(sweetness=4,milk_level=2)
my_chai.sip()
my_chai.addedSugars(3)
        
        

        