confVariable = "Plan Semilla 2023 - Data Engineering"
dictSamples = {'Peter':1000,'Safi':4000,'Arnold':5000,'Ester':100000}

def sumacion(arg1,arg2):
    return arg1 + arg2

class Perrimon:
    def __init__(self,nombre):
        self.nombre = nombre

    def ladrar(self):
        return f'el perrimon {self.nombre} dice guau!'
    
#Cuando se ejecuta como script.
if __name__  == '__main__' :
    perrito1 = Perrimon('Fernandez')
    print(perrito1.ladrar()) 
