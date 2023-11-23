""" class Galletita:
    chocolate = False

    def saludar(soy_el_propio_objeto):
        print("Hola, soy un galletita")
        print(soy_el_propio_objeto)


galleta = Galletita()
galleta.saludar()


class Galletita:
    def __init__(self):
        print("Hola, soy una galleta esta vez")


galleta = Galletita()


"Constructor"


class Galletita:
    chocolate = False

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print(f"Se creo una galletita {self.color} y {self.sabor}")


galletita_1 = Galletita("marron", "Amarga")
galletita_2 = Galletita("Negra", "Dulce")


class Galletita:
    def __init__(self):
        print("Me estoy borrando")


galleta = Galletita()
""" """ galleta.__del__() """
"""


class Galletita:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
        return f"Soy una galletita {self.color} y {self.sabor}"


galleta = Galletita("Dulce", "Rosa")
print(galleta)
print(str(galleta))
print(galleta.__str__())


class Cancion:
    def __init__(self, autor, titulo, duracion):
        self.duracion = duracion

    def __len__(self):
        return self.duracion


cancion = Cancion("Conejo Malo", "Titi me pregunto", 420)

print(len(cancion))
print(cancion.__len__())
 """
