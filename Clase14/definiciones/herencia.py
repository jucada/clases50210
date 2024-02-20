class Mamifero:
    def __init__(self, cantMamas, vida):
        self.cantMamas = cantMamas
        self.vida = vida

    def mamar(self):
        print("El animal se está amamantando")
    
    def nacer(self):
        print("El animal ha nacido! Hola Mundo!!!")

class AnimalMarino:
    def __init__(self, branqueas, especie):
        self.branqueas = branqueas
        self.especie = especie

    def nadar(self):
        print("El animal está nadando")

class Cetaceo(AnimalMarino, Mamifero):
    def __init__(self, cantMamas, vida, branqueas, especie, notas, lugar, peso):
        Mamifero.__init__(self, cantMamas, vida) #animalMarino??? Mamifero???
        AnimalMarino.__init__(self, branqueas, especie) #llamar al init del Mamifero
        self.notas = notas
        self.lugar = lugar
        self.peso = peso
    
    def nacer(self):
        print("Ha nacido un cetáceo! Hola Mundo!!!")

    def nadar(self):
        print("El cetáceo está nadando")
