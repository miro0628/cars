#skapade en klass
class car:

    #constructor

    def __init__(self, Fabrikat, color, lager):
        self.Fabrikat = Fabrikat
        self.color = color
        self.lager = lager

    def setFabrikat(self,Fabrikat):
        self.Fabrikat=Fabrikat


    def getFabrikat(self):
        return self.Fabrikat
    
    def setColor(self,Color):
        self.color=Color
    
    def getColor(self):
        return self.color