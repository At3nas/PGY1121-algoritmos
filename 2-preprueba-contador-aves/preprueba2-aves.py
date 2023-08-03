aves = ("Loro", "Avestruz", "Gallina", "Pinguino", "Canario")
numLoro = 0
numAvest = 0
numGall = 0
numPin = 0
numCan = 0

iteracion = 0

def invalidOpt(x):
    print(f"ERROR: {x} no es una opción válida. Por favor, inténtelo de nuevo.")

def main():
    print("Ha aparecido un grupo de 7 aves. ¿Qué tipo de aves observas?")
    print("")

    for num in range(0, 5, 1):
        print(f"({num}) {aves[num]}")

    while(True):
        print("")
        userAns = int(input(">> "))
        
        match userAns:
            case 0:
                numLoro += 1
            case 1:
                numAvest += 1
            case 2:
                numGall += 1
            case 3:
                numPin += 1
            case 4:
                numCan += 1
            case _:
                invalidOpt(userAns)
                continue

main()