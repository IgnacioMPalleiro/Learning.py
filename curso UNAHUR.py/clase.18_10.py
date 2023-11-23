"""Condicionar permitir el flujo de un programa en diferentes caminos"""

##IF

""" a = 5
if a ==2:
    print("A vale 2")
if a ==5:
    print("A vale 5")   
 """


""" if a ==5:
    print("A vale 5")
    if b ==10:
        print("B vale 10")
 """

""" if a == 5 or b == 1:
    print("A vale 5 y B vale 10") """

#ELSE

""" n = 11
if n ==11:
    print("N vale 11")
else:
    print("Un numero distinto a 11")

comando = "salir"

if comando == "Entrar":
    print("Bienvenido al sistema")
elif comando == "Saludar":
    print("Hola, espero que te lo estes pasando bien aprendiendo")
elif comando =="Salir":
    print("Saliendo del sistema")
else:
    print("No se reconoce") """

""" nota = float(input("Introduce tu nota"))
if nota >=9:
    print("La rompiste")
elif nota >=7 and nota < 9:
    print("Que trabajo")
elif nota >=6 and nota < 7:
    print("Esta bien...")
elif nota >=5 and nota < 6:
    print("Suficiente")
else:
    print("Desaprobaste") """
    
#                               ITERACIONES
#ITERAR significa realizar una acción varias veces. Cada vez que esto se repite se demonima una ITERACIÓN

#WHILE

""" c = 0

while c <=5:
    c+=1
    print("c vale", c)
else:
    print("Se ha completado la ITERACIÓN y c vale", c) """


#Break
""" c = 0
while c<=5:
    c+=1
    if (c==2):
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale:", c) """
    
    
#CONTINUE o saltar    

""" c = 0
while c<=5:
    c+=1
    if c==3 or c==4:
        continue
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale", c)    
     """


    
    
    