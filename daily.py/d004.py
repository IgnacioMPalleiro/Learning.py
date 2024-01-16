"""lista_colores = ["Azul", "Rojo", "Amarillo", "Verde", "Blanco"]"""

"""print(lista_colores[1][2])  """
# Primer corchete para localizar la palabra y segundo para loc. el caracter
"""print(lista_colores[-1])"""
# Se usan los negativos para buscar de atras hacia delante, 0= azul, -1=Blanco...

""" lista_colores[1] = "Naranja" """
# Para sustituir, nombramos la variable, seleccionamos la posición del color y asignamos otro.

# Para agregar otro valor a la lista utilizamos .APPEND()
"""lista_colores.append("naranja")"""

# Para agregar un nuevo valor pero controlando su posición utilizamos INSERT()
"""lista_colores.insert(2,"naranja")"""
# especificamos primero en la posición en la que se va a añadir y luego lo que queremos añadir.

# Podemos vaciar una lista con .CLEAR()
""""lista_colores.clear()"""

# Podemos eliminar un solo elemento de la lista utilizando .POP(numero de posición)

# EJERCICIOS

"""lista_numeros = [10, 45, 55, 76]"""
""" print(lista_numeros[3])"""
""" print(
    f"El valor mas pequeño en la lista es el {lista_numeros[0]} .El valor más grande, el {lista_numeros[3]}") """

"""print(lista_colores[0][2])"""

"""lista_colores = ["rojo", "azul", "verde", "amarillo"]"""


"""lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)

print(lista_colores)"""

"""lista_nueva = lista_colores
print(lista_nueva)"""

lista_numeros = [10, 45, 356, 10, 10, 10,
                 46, 67, 45, 10, 10, 43, 10, 65, 10, 10]

"""print(lista_numeros.count(10))"""

"""paises = ["Afghanistan", "Albania", "Algeria",
          "Andorra", "Angola", "Anguilla",
          "Antigua and Barbuda",
          "Argentina", "Armenia",
          "Aruba", "Australia", "Austria",
          "Azerbaijan", "Bahamas", "Bahrain",
          "Bangladesh", "Barbados", "Belarus",
          "Belgium", "Belize", "Benin", "Bermuda",
          "Bhutan", "Bolivia", "Bosnia & Herzegovina",
          "Botswana", "Brazil", "British Virgin Islands",
          "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
          "Cambodia", "Cameroon", "Cape Verde",
          "Cayman Islands", "Chad", "Chile", "China",
          "Colombia", "Congo", "Cook Islands",
          "Costa Rica", "Cote D Ivoire", "Croatia",
          "Cruise Ship", "Cuba", "Cyprus", "Czech Republic",
          "Denmark", "Djibouti", "Dominica",
          "Dominican Republic", "Ecuador", "Egypt",
          "El Salvador", "Equatorial Guinea",
          "Estonia", "Ethiopia", "Falkland Islands",
          "Faroe Islands", "Fiji", "Finland", "France",
          "French Polynesia", "French West Indies", "Gabon",
          "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar",
          "Greece", "Greenland", "Grenada", "Guam", "Guatemala",
          "Guernsey", "Guinea", "Guinea Bissau", "Guyana",
          "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland",
          "India", "Indonesia", "Iran", "Iraq", "Ireland",
          "Isle of Man", "Israel", "Italy", "Jamaica", "Japan",
          "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kuwait",
          "Kyrgyz Republic", "Laos", "Latvia", "Lebanon",
          "Lesotho", "Liberia", "Libya", "Liechtenstein",
          "Lithuania", "Luxembourg", "Macau", "Macedonia",
          "Madagascar", "Malawi", "Malaysia", "Maldives",
          "Mali", "Malta", "Mauritania", "Mauritius", "Mexico",
          "Moldova", "Monaco", "Mongolia", "Montenegro",
          "Montserrat", "Morocco", "Mozambique", "Namibia",
          "Nepal", "Netherlands", "Netherlands Antilles",
          "New Caledonia", "New Zealand", "Nicaragua", "Niger",
          "Nigeria", "Norway", "Oman", "Pakistan", "Palestine",
          "Panama", "Papua New Guinea", "Paraguay", "Peru",
          "Philippines", "Poland", "Portugal", "Puerto Rico",
          "Qatar", "Reunion", "Romania", "Russia", "Rwanda",
          "Saint Pierre & Miquelon", "Samoa", "San Marino",
          "Satellite", "Saudi Arabia", "Senegal", "Serbia",
          "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
          "Slovenia", "South Africa", "South Korea", "Spain",
          "Sri Lanka", "St Kitts & Nevis", "St Lucia",
          "St Vincent", "St. Lucia", "Sudan", "Suriname", "Swaziland",
          "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
          "Tanzania", "Thailand", "Timor L'Este", "Togo", "Tonga",
          "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan",
          "Turks & Caicos", "Uganda", "Ukraine",
          "United Arab Emirates", "United Kingdom", "Uruguay",
          "Uzbekistan", "Venezuela", "Vietnam",
          "Virgin Islands (US)", "Yemen", "Zambia", "Zimbabwe"]"""

"""print(paises.index("Brazil"))"""

lista_numeros.sort(reverse=True)
print(lista_numeros)
