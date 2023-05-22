# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro,
# un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo 
# parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena.

from functools import reduce

def reemplazarCaracteres(cadena: str, caracter1: str, caracter2: str):
     
    cadena_final = reduce(lambda x, car: x.replace(caracter1, caracter2), cadena, cadena)
    numero_reemplazos = cadena.count(caracter1)
    return numero_reemplazos, cadena_final

cadena = "Buenas tardes, como esta?"
caracter1 = "a"
caracter2 = "*"


numero_reemplazos, cadena_final = reemplazarCaracteres(cadena, caracter1, caracter2)
print("Cantidad de veces reemplazadas:", numero_reemplazos)