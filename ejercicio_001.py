"""
Ejercicio 1

Autor: Karen Beatriz León Sánchez
"""
from datetime import datetime       # Librería para obtener el tiempo

# --------------------------------------------
# Entradas
# --------------------------------------------
print("Bienvenido \nA continuación, responde las siguientes preguntas...")
# Primera pregunta
name = input("¿Cuál es tu nombre?\n:")
# Segunda pregunta
last_name1 = input("¿Cuál es tu primer apellido?\n:")
# Tercera pregunta
last_name2 = input("¿Cuál es tu segundo apellido?\n:")
# Cuarta pregunta
birth_year = int(input("¿En qué año naciste?\n:"))
# Quinta pregunta
birth_day  = input("¿En qué mes y día naciste?(en el siguiente formato mm-dd)\n:")


# --------------------------------------------
# Salidas
# --------------------------------------------
print("\n")
# A)
full_name = name + " " + last_name1 + " " + last_name2
print("A. Este es tu nombre completo en mayúsculas:",full_name.upper())

# B)
print("B. Este es tu nombre completo en minúsculas:",full_name.lower())

# C)
birth_date = birth_day[3:5] + "-" + birth_day[0:2] + "-" + str(birth_year)
print("C. Esta es tu fecha de nacimiento:",birth_date)

# D)
now = datetime.now()   # Obtener fecha actual de PC
current_year  = int(now.year)
current_month = int(now.month)
current_day   = int(now.day)

years = current_year-birth_year
if (current_month<int(birth_day[0:2]) or (current_day<int(birth_day[3:5]) and current_month<=int(birth_day[0:2]))):
    years = years-1
# End if
print("D. Esta es tu edad:",years)

# F)
i = 0
for letra in full_name:
    if letra.lower() in "aeiou":
        i += 1
    # End if
#End for

print("E. Tu nombre completo tiene ",i,"vocales")

# G) 
print("G. ¿Tu edad es un caracter de tipo de número?:",isinstance(years, int))

# H) 
cadena_alfanumerica=name+last_name1+last_name2
print("H. ¿Tu nombre completo es un carácter de tipo alfanumérico?:",cadena_alfanumerica.isalnum())

# I)
print("I. Tu edad en 10 años será:",years+10,"años")

# J)
print("J. La media de tu edad actual y tu edad en 20 años es:",(years+years+20.0)/2.0)