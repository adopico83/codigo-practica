while True:
    print("===CALCULADORA===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")



    opcion = input("Elige una operación: ")

    if opcion == "1":
        num1 = float(input("Dime el primer número: "))
        num2 = float(input("Dime el segundo número: "))
        resultado = num1 + num2
        print("Resultado:", resultado)


    elif opcion == "2":
        num1 = float(input("Dime el primer número: "))
        num2 = float(input("Dime el segundo número: "))
        resultado = num1 - num2
        print("Resultado:", resultado)


    elif opcion == "3":
        num1 = float(input("Dime el primer número: "))
        num2 = float(input("Dime el segundo número: "))
        resultado = num1 * num2 
        print("Resultado:", resultado)


    elif opcion == "4":
        num1 = float(input("Dime el primer número: "))
        num2 = float(input("Dime el segundo número: "))
        

        if num2 == 0:
            print("Error: No se puede dividir por 0")
        
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)


    elif opcion == "5":
        print("Hasta luego")
        break
    