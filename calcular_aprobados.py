aprobados = 0
nota = int(input("Dime una nota"))

while nota != -1:
    if nota >= 5:
        aprobados = aprobados + 1


    nota = int(input("Dime una nota"))

print("total de aprobados:", aprobados)