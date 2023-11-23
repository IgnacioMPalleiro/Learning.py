""" persona = {"Nombre": "Ignacio", "Apellido": "Palleiro", "Edad": 19}
persona["puede_votar"] = True
persona["Juegos_Favoritos"] = ["Minecraft", "Black Ops 3", "Age of Empires"]
persona["Juegos_Favoritos"].append("Gran Turismo")
print(persona)
del persona["Apellido"]

dic1 = {1: "uno"}
dic2 = {2: "dos"}
dic3 = {3: "tres"}

nuevo_dictionary = {}
nuevo_dictionary.update(dic1)
nuevo_dictionary.update(dic2)
nuevo_dictionary.update(dic3)
print(nuevo_dictionary)
 """


#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (sin usar max[])

from unittest import result


def custom_max (n1: int, n2: int) : 
    if n1 > n2: 
        return n1
    else:
        return n2
print(custom_max(2,3))


#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (sin usar max[])

def custom_max (n1: int, n2: int) : 
    if n1 > n2: 
        return n1
    else:
        return n2
print(custom_max(2,3))


def función_de_tres_max(n1, n2, n3):
    if n1 > n2 > n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else: 
        return n3
print(función_de_tres_max(3123, 4314, 6666))

#def una función que tome un caracter y si es una vocal que devuelva True, si no que devuelva False
def letra_vocal(caracter):
    lista_vocales = ["a","e","i","o","u"]
    if caracter in lista_vocales:
        return True
    else:
        return False
print(letra_vocal("a"))


""" def suma(lista):   
    resultado = 0
    for n in lista:
        resultado = resultado + n
    return resultado

mi_lista = [-77, 634, 56]
resultado = suma(mi_lista)
print(resultado) """

def multiplico(lista):
    resultado = 1
    i = 0
    while i < len(lista):
        resultado = resultado * lista[i]
        i += 1
        print(resultado)
        
multiplico([3,2,3])