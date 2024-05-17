import Pyro4

uri_calculator = Pyro4.Proxy("PYRO:obj_be59e7f822be43cf8898af4315d03e73@localhost:46769")

while True:
    print("Menu")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
    
    opcion = input("Opción => ")
    
    if opcion == "1":
        numero1 = float(input("Ingrese el primer número => "))
        numero2 = float(input("Ingrese el segundo número => "))
        print("Resultado:", uri_calculator.sumar(numero1, numero2))
    elif opcion == "2":
        numero1 = float(input("Ingrese el primer número => "))
        numero2 = float(input("Ingrese el segundo número => "))
        print("Resultado:", uri_calculator.restar(numero1, numero2))
    elif opcion == "3":
        numero1 = float(input("Ingrese el primer número => "))
        numero2 = float(input("Ingrese el segundo número => "))
        print("Resultado:", uri_calculator.multiplicar(numero1, numero2))
    elif opcion == "4":
        numero1 = float(input("Ingrese el primer número => "))
        numero2 = float(input("Ingrese el segundo número => "))
        print("Resultado:", uri_calculator.dividir(numero1, numero2))
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
