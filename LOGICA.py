class Vehiculo:

    def __init__(self, nombre, color):
        self.__nombre = nombre
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getNombre(self):
        return self.__nombre


class Auto(Vehiculo):

    def __init__(self, nombre, color, modelo):
        super().__init__(nombre, color)
        self.__modelo = modelo

    def getDescripcion(self):
        return self.getNombre() + self.__modelo + " de color " + self.getColor()


c = Auto("camaro", "negro", "ZL1")
print(c.getDescripcion())
print(c.getNombre()) 