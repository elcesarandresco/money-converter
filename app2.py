dolar = [" ",3800, 99.70, 20.56]

def conversor (moneda, monto):
    calculo = monto / moneda;
    calculo = str(round(calculo, 2))
    print("Usted tiene $" + calculo + " USD")

def frase (divisa):
    return "¿Cuantos " + divisa + " quiere convertir a dólares?: "


menu = """

#############################################################################

Bienvenido al conversor de monedas a dólares, elija una divisa para comenzar:

1. Pesos Colombianos
2. Pesos Mexicanos
3. Pesos Argeninos

#############################################################################

"""
opcion = int(input(menu))

if opcion == 1:

    moneda = dolar[1]
    divisa = "Pesos Colombianos"
    monto = float(input(frase(divisa)))
    

elif opcion == 2:

    moneda = dolar[3]
    divisa = "Pesos Mexicanos"
    monto = float(input(frase(divisa)))

elif opcion == 3:

    moneda = dolar[2]
    divisa = "Pesos Argentinos";
    monto = float(input(frase(divisa)))

else:
    print("Ingrese un tipo de moneda válido")
    exit()


conversor(moneda, monto)

