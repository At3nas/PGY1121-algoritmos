# Contador de ovejas
contOvejas = 0

# Colores de ovejas
colorOvejas = ["Negra", "Blanca", "Morada", "Verde", "Amarillo", "Rojo", "Lobo"]
# Nro de ovejas por grupo
numOvejasGrupo = [0, 0, 0, 0, 0, 0, 0]
# Nro de ovejas totales
numOvejasTotal = [0, 0, 0, 0, 0, 0, 0]
# Precio de cada oveja
precioOvejas = (800, 1200, 3000, 2670, 1500, 3410)

# Muestra tabla de ovejas
def tablaOvejas():
    print("Color de oveja | Ovejas vendidas | Precios")
    print("---------------|-----------------|--------------")
    print(f"{colorOvejas[0]}          | {numOvejasTotal[0]}               | ${precioOvejas[0]}")
    print(f"{colorOvejas[1]}         | {numOvejasTotal[1]}              | ${precioOvejas[1]}")
    print(f"{colorOvejas[2]}         | {numOvejasTotal[2]}               | ${precioOvejas[2]}")
    print(f"{colorOvejas[3]}          | {numOvejasTotal[3]}               | ${precioOvejas[3]}")
    print(f"{colorOvejas[4]}       | {numOvejasTotal[4]}               | ${precioOvejas[4]}")
    print(f"{colorOvejas[5]}           | {numOvejasTotal[5]}               | ${precioOvejas[5]}")

# Calcula ganancia por ventas
def ganaciaVentas():
    print("--------------- TABLA DE PRECIOS ---------------")
    tablaOvejas()
    print("------------- GANANCIAS POR VENTAS -------------")
    print("$" , (numOvejasTotal[0] * precioOvejas[0]) + (numOvejasTotal[1] * precioOvejas[1]) + (numOvejasTotal[2] * precioOvejas[2]) + (numOvejasTotal[3] * precioOvejas[3]) + (numOvejasTotal[4] * precioOvejas[4]) + (numOvejasTotal[5] * precioOvejas[5]))
    print("------------------------------------------------")

# Cuenta ovejas por grupo
def contarOvejasGrupo():
    global contOvejas
    contOvejas = 0
    print("")
    print("Ingrese los colores de las ovejas que conforman el grupo:")
    while (contOvejas <= 9):
        userInp = int(input(">> "))
        contOvejas += 1

        match userInp:
            case 0:
                numOvejasGrupo[0] += 1
            case 1:
                numOvejasGrupo[1] += 1
            case 2:
                numOvejasGrupo[2] += 1
            case 3:
                numOvejasGrupo[3] += 1
            case 4:
                numOvejasGrupo[4] += 1
            case 5:
                numOvejasGrupo[5] += 1
            case 6:
                print("Apareció un lobo y ahuyentó a las ovejas.")
                break
            
        if (numOvejasGrupo[0] > 6):
            print("Hay más de 6 ovejas negras.")
            print("")
            ganaciaVentas()
            break
        elif (numOvejasTotal[2] > numOvejasTotal[3]):
            print("Hay más ovejas moradas que verdes.")
            print("")
            ganaciaVentas()
            break
        elif (numOvejasGrupo[5] > 30):
            print("Hay más de 30 ovejas rojas.")
            ganaciaVentas()
            break

# PROGRAMA
print("Un grupo puede tener ovejas de los siguientes colores:")
for num in range(0, len(colorOvejas), 1): # imprime la lista de ovejas para el menu
    print(f"({num}) {colorOvejas[num]}")

contarOvejasGrupo()

for num in range(0, 6, 1):
    numOvejasTotal[num] = numOvejasGrupo[num]

for num in range(0, 6, 1):
    numOvejasGrupo[num] = 0

print("")
print("¿Desea seguir la cuenta?")
print("(0) No")
print("(1) Sí")
userInp = int(input(">> "))

if (userInp == 0):
    ganaciaVentas()
elif (userInp == 1):
    contarOvejasGrupo()
else:
    print("Por favor, ingrese una opción válida.")

