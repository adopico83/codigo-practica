numero1 = int(input("escribe el primer número"))
numero2 = int(input("escribe el segundo número"))

operacion = input("Operacion (sumar/restar/multiplicar/dividir): ")

if operacion == "sumar":
    resultado = numero1 + numero2

elif operacion == "restar":
    resultado = numero1 - numero2

elif operacion == "multiplicar":
    resultado = numero1 * numero2

elif operacion == "dividir":
    resultado = numero1 / numero2

print("resultado:", resultado)