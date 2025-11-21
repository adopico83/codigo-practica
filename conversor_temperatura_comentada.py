# CONVERSOR DE TEMPERATURA - EJERCICIO 10
# Programa que convierte entre Celsius y Fahrenheit

# Bucle infinito - se repite hasta que usuario elija salir (opción 3)
while True:
    
    # ===== MOSTRAR MENÚ =====
    # Imprimimos las opciones disponibles para el usuario
    print("=== CONVERSOR TEMPERATURA ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")
    
    # Pedimos al usuario que elija una opción (se guarda como texto/string)
    opcion = input("Elige opción: ")
    
    # ===== OPCIÓN 1: CELSIUS A FAHRENHEIT =====
    if opcion == "1":
        # Pedimos temperatura en Celsius y la convertimos a decimal (float)
        celsius = float(input("Temperatura en Celsius: "))
        
        # Aplicamos la fórmula de conversión: F = (C × 9/5) + 32
        fahrenheit = (celsius * 9/5) + 32
        
        # Mostramos el resultado con el símbolo de grado Fahrenheit
        print("Temperatura en Fahrenheit:", fahrenheit, "°F")
    
    # ===== OPCIÓN 2: FAHRENHEIT A CELSIUS =====
    elif opcion == "2":
        # Pedimos temperatura en Fahrenheit y la convertimos a decimal (float)
        fahrenheit = float(input("Temperatura en Fahrenheit: "))
        
        # Aplicamos la fórmula de conversión: C = (F - 32) × 5/9
        celsius = (fahrenheit - 32) * 5/9
        
        # Mostramos el resultado con el símbolo de grado Celsius
        print("Temperatura en Celsius:", celsius, "°C")
    
    # ===== OPCIÓN 3: SALIR =====
    elif opcion == "3":
        # Mensaje de despedida
        print("Hasta luego")
        # break ROMPE el bucle while - el programa termina aquí
        break
    
    # ===== OPCIÓN INVÁLIDA =====
    # Si el usuario escribe algo que NO es 1, 2 o 3
    else:
        print("Opción inválida")
    
    # Después de cada conversión, el bucle vuelve al principio (while True)
    # y muestra el menú de nuevo, EXCEPTO si se ejecutó el break

# FIN DEL PROGRAMA
# Esta línea solo se alcanza si se ejecutó el break (opción 3)