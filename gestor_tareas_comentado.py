# GESTOR DE TAREAS CON COMENTARIOS EXPLICATIVOS

tareas = []  # Lista vacía para guardar todas las tareas

while True:  # Bucle infinito hasta que usuario elija salir
    # Mostrar el menú de opciones
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar completada")
    print("4. Salir")
    
    opcion = input("Elige opción: ")  # Pedir opción al usuario
    
    # OPCIÓN 1: AÑADIR TAREA
    if opcion == "1":
        tarea = input("Escribe la tarea: ")  # Pedir la tarea
        tareas.append(tarea)  # Añadir tarea a la lista
        print("Tarea añadida")  # Confirmar al usuario
    
    # OPCIÓN 2: VER TAREAS
    elif opcion == "2":
        if len(tareas) == 0:  # Comprobar si la lista está vacía
            print("No hay tareas pendientes")
        else:
            print("\n=== TUS TAREAS ===")
            # Recorrer la lista y mostrar cada tarea numerada
            for i in range(len(tareas)):  # i = 0, 1, 2...
                print(i + 1, ".", tareas[i])  # i+1 para mostrar 1, 2, 3...
    
    # OPCIÓN 3: MARCAR COMPLETADA (ELIMINAR)
    elif opcion == "3":
        if len(tareas) == 0:  # Verificar si hay tareas
            print("No hay tareas para completar")
        else:
            print("\n=== TUS TAREAS ===")
            # Mostrar todas las tareas numeradas
            for i in range(len(tareas)):
                print(i + 1, ".", tareas[i])
            
            # Pedir número de tarea y convertir a entero
            numero = int(input("\n¿Qué tarea completaste? (número): "))
            
            # Validar que el número esté en el rango correcto
            if numero >= 1 and numero <= len(tareas):  # Entre 1 y total de tareas
                # Eliminar tarea (numero-1 porque las listas empiezan en 0)
                # .pop() elimina Y devuelve el elemento
                tarea_completada = tareas.pop(numero - 1)
                print("Tarea completada:", tarea_completada)  # Confirmar
            else:
                print("Número de tarea inválido")  # Número fuera de rango
    
    # OPCIÓN 4: SALIR
    elif opcion == "4":
        print("Hasta luego")
        break  # Sale del bucle while (termina el programa)
    
    # OPCIÓN INVÁLIDA
    else:
        print("Opción inválida")  # Cualquier otra opción