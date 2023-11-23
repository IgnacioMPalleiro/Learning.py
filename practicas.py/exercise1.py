#Ejercitación

""" Escribir un programa que pregunte el nombre del usuario en 
la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
donde <nombre> es el nombre que el usuario haya introducido.
 """

""" nombre = (input("Cual es tu nombre?"))

print("¡Hola " + nombre + "!") """


""" Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
 """

""" horas_trabajadas = float(input("Horas trabajadas"))
coste_por_hora = float(input("costo por hora"))

pago = horas_trabajadas * coste_por_hora

print(pago) """


""" Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
es el índice de masa corporal calculado redondeado con dos decimales.
 """
 
peso = (input("introduzca su peso"))
altura = (input("Introduzca su altura"))

IMC = round(float(peso)/float(altura)**2,2)

print("Su IMC es de " + str(IMC))



