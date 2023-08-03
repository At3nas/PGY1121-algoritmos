#------ NO CAMBIAR ----------------------------------------#
from autoHerramientas import *
#---------------------------------------------------------#
#puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "Autos1"

#puede cambiar la forma de la lista entre:
#lista de diccionario -> tipo_lista = "diccionario"
#lista de listas -> tipo_lista = "lista"
tipo_lista = "lista"

lista_autos = obtenerAutos(nombre_archivo,tipo_lista)

#---------------------------------------------------------#

menuOpciones = ("Buscar auto por modelo", "Imprimir lista",
"Imprimir certificado", "Buscar auto por patente", "Buscar por rango de año",
"Agregar información de dueño al auto", "Mostrar todos los autos del color favorito",
"Salir")


# PREGUNTA DATOS AL USUARIO
def userData():
    print("--------------- DATOS DEL USUARIO ------------")
    print("")
    nombre_usuario = str(input("Nombre de usuario: "))
    fecha_actual = str(input("Fecha actual: "))
    color_favorito = str(input("Color favorito: "))
    print("")

    return nombre_usuario, fecha_actual, color_favorito

# IMPRIME LOS AUTOS
def imprimirAutos(auto:list):
    for i in range(0, len(auto), 1):
        print(f"--------------- AUTO {i+1} ------------")
        print(f"Marca: {auto[i][0]}")
        print(f"Modelo: {auto[i][1]}")
        print(f"Año: {auto[i][2]}")
        print(f"Patente: {auto[i][3]}")
        print(f"Color: {auto[i][4]}")

# BUSCAR AUTO POR MODELO
def buscarModelo(lista_autos:list, modelo_auto:str):
    autosModelo = []
    for auto in lista_autos: # recorre la lista de autos
        if (auto[1] == modelo_auto): # si coinciden los modelos, se insertan los autos a la lista
            autosModelo.append(auto)
    return autosModelo

# BUSCAR AUTO POR PARAMETRO
def buscarParam(lista_autos:list, llave, param):
    autosParam = []
    for auto in lista_autos: # recorre lista de autos
        match llave:
            case 1: #marca
                if (auto[0] == param):
                    autosParam.append(auto)
            case 2: #modelo
                if (auto[1] == param):
                    autosParam.append(auto)
            case 3: #año
                if (auto[2] == param):
                    autosParam.append(auto)
            case 4: #patente
                if (auto[3] == param):
                    autosParam.append(auto)
            case 5: #color
                if (auto[4] == param):
                    autosParam.append(auto)
    return autosParam

# BUSCAR AUTO POR PATENTE
def buscarPatente(lista_autos:list, patente_auto):
    autosPatente = []
    for auto in lista_autos:
        if (auto[3] == patente_auto):
            autosPatente.append(auto)
    return autosPatente

# BUSCAR AUTO POR RANGO DE AÑO
# NOTA: NO FUNCIONAL
def buscarAño(lista_autos:list, año1:int, año2:int):
    autosAño = []
    for auto in lista_autos:
        if (auto[2] == año1 or auto[2] == año2):
            autosAño.append(auto)
    return autosAño

# BUSCAR AUTO POR COLOR FAVORITO
def buscarColorFav(lista_autos:list, color_favorito):
    autosColorFav = []
    for auto in lista_autos:
        if (auto[4] == color_favorito):
            autosColorFav.append(auto)
    return autosColorFav

# MUESTRA MENU DE OPCIONES
def menu(nombre_usuario, fecha_actual, color_favorito):
    print("-------------------- MENU --------------------")
    print("")
    for i in range(0, len(menuOpciones), 1):
        print(f"{i+1} | {menuOpciones[i]}")
    print("")

    selecOp(nombre_usuario, fecha_actual, color_favorito)

# VALIDA LA OPCION QUE SELECCIONA EL USUARIO
def selecOp(nombre_usuario, fecha_actual, color_favorito):
    selec = int(input(">> "))

    match selec:
        case 1: # buscar auto por modelo
            print("-------------------- BUSCAR AUTO POR MODELO --------------------")
            print("")
            modelo_auto = str(input("Ingrese el modelo: "))
            autosModelo = buscarModelo(lista_autos, modelo_auto)
            if (autosModelo != None):
                imprimirAutos(autosModelo)
            else:
                print(f"No se encontraron autos del modelo {modelo_auto}")

            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)
        case 2: # imprimir lista
            llavesOp = ("Marca","Modelo","Año", "Patente", "Color")
            print("-------------------- IMPRIMIR LISTA --------------------")
            print("")
            for i in range(0, len(llavesOp), 1):
                print(f"{i+1} | {llavesOp[i]}")
            print("")
            llave = int(input(">> Ingrese una llave: "))
            param = str(input(">> Ingrese el parámetro: "))
            print("")
            autosParam = buscarParam(lista_autos, llave, param)
            imprimirAutos(autosParam)
            
            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)
        case 3: # imprimir certificado
            print("-------------------- IMPRIMIR CERTIFICADO --------------------")
            print("")
            imprimirAutos(lista_autos)
            print("")
            selec = int(input(">> Número del auto: "))
            print("")

            print(f'''{nombre_usuario} emite certificado que:
        El vehiculo {lista_autos[selec-1][0]} {lista_autos[selec-1][1]} con patente {lista_autos[selec-1][3]}
        De color {lista_autos[selec-1][4]}
        Queda registrado oficialmente a la fecha de {fecha_actual}''')
        
            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)
        case 4: # buscar auto por patente
            print("-------------------- BUSCAR AUTO POR PATENTE -----")
            print("")
            patente_auto = str(input("Ingrese la patente: "))
            autosPatente = buscarPatente(lista_autos, patente_auto)
            if (autosPatente != None):
                imprimirAutos(autosPatente)
            else:
                print(f"No se encontraron autos con la patente {patente_auto}")

            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)
        case 5: # buscar por rango de año (NO IMPLEMENTADO)
            print("-------------------- BUSCAR AUTO POR RANGO DE AÑO -----")
            print("")
            print("Ingrese dos años:")
            año1 = int(input(">> Desde: "))
            año2 = int(input(">> Hasta: "))

            autosAño = buscarAño(lista_autos, año1, año2)
            if (autosAño != None):
                imprimirAutos(autosAño)

            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)
        case 6: # agregar info del dueño (NO IMPLEMENTADO)
            print("-------------------- AGREGAR INFORMACIÓN DEL DUEÑO -----")
        case 7: # mostrar autos del color favorito
            print("-------------------- AUTOS DEL COLOR FAVORITO -----")
            print("")
            autosColorFav = buscarColorFav(lista_autos, color_favorito)

            if (autosColorFav != None):
                imprimirAutos(autosColorFav)
            else:
                print(f"No se encontraron autos de color {color_favorito}")

            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)
        case 8: # salir
            print("El programa ha finalizado.")
        case _:
            print("ERROR: Opción inválida. Por favor, ingrese un número del 1 al 8.")
            print("")
            menu(nombre_usuario, fecha_actual, color_favorito)

# FUNCION PRINCIPAL
def main():
    usuario = userData()
    nombre_usuario = usuario[0]
    fecha_actual = usuario[1]
    color_favorito = usuario[2]

    menu(nombre_usuario, fecha_actual, color_favorito)

main()

