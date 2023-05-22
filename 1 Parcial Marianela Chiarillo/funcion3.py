# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y 
# su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos 
# "algoritmo" la deja como "agilmoort"
def ordenarCaracteres(cadena: str, ascendente=True):
    tam = len(cadena)
    cadena_list = list(cadena)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (ascendente and cadena_list[i] > cadena_list[j]) or (not ascendente and cadena_list[i] < cadena_list[j]):
                aux = cadena_list[i]
                cadena_list[i] = cadena_list[j]
                cadena_list[j] = aux

    cadena_ordenada = ''.join(cadena_list)
    return cadena_ordenada

cadena = "hola"
cadena_ordenada = ordenarCaracteres(cadena)
print("Cadena ordenada:", cadena_ordenada)