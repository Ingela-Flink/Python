#Detta är en klass man kan skapa objekt av
class Bil:
    
    def __init__(self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager

    #funktioner som tillhör en klass kallas metoder
    def setFabrikat(self, fabrikat):
        self.fabrikat = fabrikat

    def getFabrikat(self):
        return self.fabrikat
        
    def getLager(self):
        return self.lager
        
    def getColor(self):
        return self.color
    
    def setLager(self, lager):
        self.lager = lager