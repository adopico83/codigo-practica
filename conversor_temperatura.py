while True:

    print("=== CONVERSOR TEMPERATURA ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")


    opcion = input("Elige opción: ")


    if opcion == "1":
        celsius = float(input("Temperatura en Celsius: "))

        fahrenheit = (celsius * 9/5) + 32

        print(f"Temperatura Fahrenheit: , {fahrenheit}ºF")


    elif opcion == "2":
        fahrenheit = float(input("Temperatura en Fahrenheit: "))

        celsius = (fahrenheit - 32) * 5/9

        print(f"Temperatura Celsius: , {celsius}ºC")


    elif opcion == "3":
        print("Hasta luego")
        break

    else: 
        print("Opción invalida")
    