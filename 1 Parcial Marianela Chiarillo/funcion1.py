#1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva 
#el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicar_aumento(precio:float):
    aumento = precio *5/100
    precio_aumentado = precio + aumento
    return precio_aumentado

precio = float(input("Ingrese un valor y se le agregara el aumento-> "))
precio_final = aplicar_aumento(precio)
print(precio_final)



