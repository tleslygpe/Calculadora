while True:
  print("Mi calculadora")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Suma Avanzada")
  print("")
  opcion_seleccionada = input(int("¿Que deseas hacer?: ")

  if opcion_seleccionada == 1:
    print("******* SUMAR *******")
    numero1 = input(int("Dime el primer número: ")
    numero2 = input(int("Dime el segundo número: ")
    resultado = sumar(numero1, numero2)
    print("El resultado es: " resultado)
    pass

  if opcion_seleccionada == 2:
    print("******* RESTAR *******")
    numero1 = input(int("Dime el primer número: ")
    numero2 = input(int("Dime el segundo número: ")
    resultado = restar(numero1, numero2)
    print("El resultado es: " resultado)
    pass
    
  if opcion_seleccionada == 3:
    print("******* MULTIPLICAR *******")
    numero1 = input(int("Dime el primer número: ")
    numero2 = input(int("Dime el segundo número: ")
    resultado = multiplicar(numero1, numero2)
    print("El resultado es: " resultado)
    pass
    
  if opcion_seleccionada == 4:
    print("******* DIVIDIR *******")
    numero1 = input(int("Dime el primer número: ")
    numero2 = input(int("Dime el segundo número: ")
    resultado = dividir(numero1, numero2)
    print("El resultado es: " resultado)
    pass
    
  if opcion_seleccionada == 5:
    print("******* SUMA AVANZADA *******")
    lista = input("Escribe los números a sumar separados por una coma (,): ")
    resultado = suma_avanzada(numero1, numero2)
    print("El resultado es: " resultado)
    pass
    
