cop = 3800
arg = 99.70
mxn = 20.56
divisa = [" ","Colombianos", "Mexicanos", "Argentinos"]
menu = """

#############################################################################

Bienvenido al conversor de monedas a dólares, elija una divisa para comenzar:

1. Pesos Colombianos
2. Pesos Mexicanos
3. Pesos Argeninos

#############################################################################

"""
opcion = input(menu)

if opcion == '1':
    
    monto = float(input("¿Cuantos pesos "+ divisa[int(opcion)] + " quiere quiere convertir?: "))
    calculo = monto / cop
    calculo = round(calculo, 2)
    print("Usted tiene $" + str(calculo) + " USD")

elif opcion == '2':

    monto = float(input("¿Cuantos pesos "+ divisa[int(opcion)] + " quiere quiere convertir?: "))
    calculo = monto / mxn
    calculo = round(calculo, 2)
    print("Usted tiene $" + str(calculo) + " USD")    

elif opcion == '3':

    monto = float(input("¿Cuantos pesos "+ divisa[int(opcion)] + " quiere quiere convertir?: "))
    calculo = monto / arg
    calculo = round(calculo, 2)
    print("Usted tiene $" + str(calculo) + " USD")    

else:

    print("Usted ha ingresado un valor erróneo, intente de nuevo.")
