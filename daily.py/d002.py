""" palabra = "Automáticamente"
print(palabra[5]) """

""" print(10**5)
"""
""" numero = 10*10*10*10*10
print(numero)
"""
# En que dos estados puedes estar un dato bool?

True or False

""" numero = 675.87 

print(type(numero)) """

""" numero = 768763843

print(len(str(numero)))
"""
# Se realiza la conversión a float

""" numero_1 = float("14.527")
numero_2 = float("560.92") """

# Se realiza la conversión a int
""" 
print(int(numero_1))
print(int(numero_2))
"""
# Redondear con los decimales pedidos en los comentarios
""" numero_1 = 10.897654876534  # 3 decimales
numero_2 = 7674.7886  # 2 decimales
numero_3 = 67854.78  # 1 decimal

print(round(numero_1, 3))
print(round(numero_2, 2))
print(round(numero_3, 1)) """

# Diferencia entre un Modulo y un Floor division
""" operación = 15 // 4 
print(operación) """

# Operadores de incremento o decremento

""" numero_1 = 10  # +60
numero_2 = 24  # -100
numero_3 = 65.67  # +4.33

numero_1 += 60
numero_2 -= 100
numero_3 += 4.33

print(numero_1)
print(numero_2)
print(numero_3)
"""
# Tecnica de formateo de Strings mediante prefijo

""" numero_1 = 4
numero_2 = 769.97
texto = "Am i a string"
decisión = True

print(f"El valor {numero_2} es bastante mas grande que {numero_1}. ¿{texto}? The answer is {decisión}.")
 """

# Calculadora de exponentes

print("--- Calculadora de exponentes ---")
numero_1 = int(input("Introduzca el primer numero:\n"))
numero_2 = int(input("Introduzca el segundo numero:\n"))

resultado = numero_1 ** numero_2
print(f"El resultado de {numero_1} elevado a {numero_2} es {resultado}")
