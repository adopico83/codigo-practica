numero = int(input("Cuántos numeros quieres?"))
pares = 0
impares = 0


for i in range(numero):
    n = int(input("Numero: "))

    if n % 2 == 0:
        pares = pares + 1

    else:
        impares = impares + 1


print("Pares:", pares)
print("Impares:", impares)