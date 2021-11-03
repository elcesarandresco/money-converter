# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")
def saludar(eleccion):
    if eleccion <= 3:
        print('Hola')
        print('¿Cómo estás?')
        print('Elegiste la opción', eleccion)
        print('Adiós')
    else:
        print("Escribe la opción correcta")


opcion = int(input("Elige una opción (1, 2, 3): "))
saludar(opcion)


