# VARIABLES
numDay = 0 # dia de la semana
shopMoney = 0 # ganancias de la tienda

# DATA STRUCTURES
# dias de la semana
weekDays = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
# animales con descuento los lunes
discMon = ("Gato", "Perro", "Erizo", "Ornitorrinco")
# animales con descuento los viernes
discFri = ("Jirafa", "Cocodrilo", "Huron", "Casuario", "Conejo")
# animales con descuento los domingos
discSun = ("Conejo", "Cuyi", "Liebre", "Suricata", "Tejon")

class Product: # crear clase producto
    # inicializar objetos de la clase producto
    def __init__(self, name, price, amount):
        self.name = name # nombre del producto
        self.price = price # precio del producto
        self.amount = amount # cantidad del producto

    def amountDecrease(self, buyAmount):
        self.amount -= buyAmount

    def netPrice(self, buyAmount):
        totalPay = self.price * buyAmount
        return totalPay

# objetos productos
product1 = Product("CatChow", 2500, 4)
product2 = Product("DogChow", 2500, 3)
product3 = Product("CasuarioChow", 4000, 4)
product4 = Product("Juguete con catnip", 1000, 10)
product5 = Product("Pelota de tenis", 600, 10)
product6 = Product("Collar para tejones", 12340, 1)

# mensaje de error:
def invalidInp(x):
    print(f"ERROR: {x} no es una opción válida. Por favor, inténtelo de nuevo.")

# mensaje de total a pagar
def totalPay(totalPay):
    print(f"Total a pagar: {totalPay}")

# permite responder 'si' o 'no' al usuario
def userOpt():
    print("(0) No")
    print("(1) Sí")
    userAns = int(input(">> "))
    return userAns

# valida si hay clientes en un dia
def validClient():
    print("¿Hay clientes hoy?")
    userAns = userOpt()
    return userAns

# validar datos del cliente
def clientData(): 
    clientName = str(input("Nombre: "))
    clientAnimal = str(input("Animal: "))
    return clientName, clientAnimal

# validar datos de la compra
def clientBuy():
    buyProd = int(input(">> Producto: "))
    buyAmount = int(input(">> Cantidad: "))
    return buyProd, buyAmount

# validar el producto a comprar por el cliente
def validProduct():
    buyData = clientBuy() # pregunta al cliente el producto y la cantidad
    buyProd = buyData[0] # producto del cliente
    buyAmount = buyData[1] # cantidad del producto

    # validamos el producto del usuario
    match buyProd:
        case 1:
            buyProd = product1.name
            netPrice = product1.price * buyAmount
            product1.amountDecrease(buyAmount)
        case 2:
            buyProd = product2.name
            netPrice = product2.price * buyAmount
            product2.amountDecrease(buyAmount)
        case 3:
            buyProd = product3.name
            netPrice = product3.price * buyAmount
            product3.amountDecrease(buyAmount)
        case 4:
            buyProd = product4.name
            netPrice = product4.price * buyAmount
            product4.amountDecrease(buyAmount)
        case 5:
            buyProd = product5.name
            netPrice = product5.price * buyAmount
            product5.amountDecrease(buyAmount)
        case 6:
            buyProd = product6.name
            netPrice = product6.price * buyAmount
            product6.amountDecrease(buyAmount)
        case _:
            invalidInp(buyProd)
    return netPrice # retorna el valor neto

# muestra catalogo de productos
def catalogue():
    print("-------------------------- CATÁLOGO --------------------------")
    print("    Producto            |    Precio   |    Cantidad")
    print("--------------------------------------------------------------")
    print(f"(1) {product1.name}             |   ${product1.price}     | {product1.amount} unidades")
    print(f"(2) {product2.name}             |   ${product2.price}     | {product2.amount} unidades")
    print(f"(3) {product3.name}        |   ${product3.price}     | {product3.amount} unidades")
    print(f"(4) {product4.name}  |   ${product4.price}     | {product4.amount} unidades")
    print(f"(5) {product5.name}     |   ${product5.price}      | {product5.amount} unidades")
    print(f"(6) {product6.name} |   ${product6.price}    | {product6.amount} unidades")

# calcula descuento
def calcDisc(price, perc):
    return price * ((100 - perc) / 100)

# funcion main
def main():
    global numDay
    while(True):
        print(f"--------------------------- {weekDays[numDay].upper()} ---------------------------")
        userAns = validClient()
        
        if (userAns == 0):
            numDay += 1
            continue
        elif (userAns == 1):
            client = clientData()
            clientName = client[0] # nombre del cliente
            clientAnimal = client[1] # tipo de animal de cliente

            catalogue() # muestra el catalogo de productos
            netPrice = validProduct()

            match numDay:
                case 0: # lunes
                    if (clientAnimal.capitalize() in discMon):
                        totalPay(calcDisc(netPrice, 20))
                    else:
                        totalPay(netPrice)
                case 1: # martes
                    totalPay(netPrice)
                case 2: # miercoles
                    if (netPrice > 30000):
                        totalPay(calcDisc(netPrice, 15))
                    else:
                        totalPay(netPrice)
                case 3: # jueves
                    totalPay(netPrice)
                case 4: # viernes
                    if (clientAnimal.capitalize() in discFri):
                        totalPay(calcDisc(netPrice, 20))
                    else:
                        totalPay(netPrice)
                case 5: # sabado
                    if (len(clientName) <= 15):
                        nameDisc = len(clientName) * 2
                        totalPay(calcDisc(netPrice, nameDisc))
                    else:
                        totalPay(calcDisc(netPrice, 30))
                case 6: # domingo
                    if (clientAnimal.capitalize() in discSun and netPrice > 40000):
                        totalPay(calcDisc(netPrice, 25))
                    else:
                        totalPay(netPrice)
        else:
            invalidInp(userAns)

# llama a funcion main
main()