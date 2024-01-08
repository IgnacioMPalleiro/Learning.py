# CALCULADORA GOD -- GOD CALCULATOR
print("!Welcome to the GOD CALCULATOR¡")
print("-------------------------------")

print("Please choose between this options:")
operator = input(
    "1-suma.\n2-resta.\n3-multiplicación.\n4-division.\n5-Modulo.\n6-exponente.\n")


num_1 = float(input("Escriba el primer operador: "))
num_2 = float(input("Escriba el segundo operador: "))

if operator == "1":
    resultado1 = round(num_1 + num_2, 2)
    print("El resultado es:", resultado1)
elif operator == "2":
    resultado2 = round(num_1 - num_2, 2)
    print("El resultado es:", resultado2)
elif operator == "3":
    resultado3 = round(num_1 * num_2, 2)
    print("El resultado es:", resultado3)
elif operator == "4":
    resultado4 = round(num_1 / num_2, 2)
    print("El resultado es:", resultado4)
elif operator == "5":
    resultado5 = round(num_1 % num_2, 2)
    print("El resultado es:", resultado5)
elif operator == "6":
    resultado6 = round(num_1 // num_2, 2)
    print("El resultado es:", resultado6)
else:
    print("Invalido, intente de vuelta.")
