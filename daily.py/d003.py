# Condicionales: Estructura de codigos para que el programa sea mas
# inteligente y pueda tomar decisiones.

# > : mayor que
# < : menor que
# == : igual que
# >= : mayor o igual
# <= : menor o igual
# != : diferente que


numero = 10


""" # Si: se ejecuta el codigo / No: se descarta el IF y pasa al Elif.
if numero > 7:
    print("El numero es mayor que 7")
# Si: se ejecuta el codigo / No: se descarta el Elif y pasa al Else.
elif numero == 7:
    print("El numero es igual a 7")
else:  # ELSE solo se ejcuta cuando IF y ELIF son falsos.
    print("El numero es menor que 7")
 """


edad = int(input("Introduzca su edad:"))

respuesta = None
respuesta_2 = None
if edad >= 18:
    print("Felicidades loquito ya podes ir preso, que vas a llevar?")
    respuesta = input("1- Cerveza. \n2- Blue Label.\n3- Fernet.\n")
    if respuesta == "1":
        print("Agarrate la que quieras pa")
        respuesta_2 = input("1- Quilmes.\n2- Brahama\n3- Corona\n")
        if respuesta_2 == "1":
            print("Vo so de barrio loco aguante Quilmes.")
        elif respuesta_2 == "2":
            print("Una Brahama bien fria loco para vos toma.")
        elif respuesta_2 == "3":
            print("Tipico chetito de capital si tomas Corona")
        else:
            print("Respuesta invalida")
    elif respuesta == "2":
        print("Elegiste el ELISIR vo si que sabe")
    elif respuesta == "3":
        print("Nada mejor cuando hace calor que un buen fernecito con hielo")
    else:
        print("No se que quisiste decir loco, repetime")
else:
    print("Raja de aca loco sos menor")
