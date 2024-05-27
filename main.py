while True:
  print("")
  print("Mi calculadora")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Suma Avanzada")
  print("")
  opcion_seleccionada = int(input("¿Que deseas hacer?: "))

  if opcion_seleccionada == 1:
    print("******* SUMAR *******")
    numero1 = int(input("Dime el primer número: "))
    numero2 = int(input("Dime el segundo número: "))
    resultado = sumar(numero1, numero2)
    print("*** El resultado es: ", resultado)

  if opcion_seleccionada == 2:
    print("******* RESTAR *******")
    numero1 = int(input("Dime el primer número: "))
    numero2 = int(input("Dime el segundo número: "))
    resultado = restar(numero1, numero2)
    print("*** El resultado es: ", resultado)
    
  if opcion_seleccionada == 3:
    print("******* MULTIPLICAR *******")
    numero1 = int(input("Dime el primer número: "))
    numero2 = int(input("Dime el segundo número: "))
    resultado = multiplicar(numero1, numero2)
    print("*** El resultado es: ", resultado)
    
  if opcion_seleccionada == 4:
    print("******* DIVIDIR *******")
    numero1 = int(input("Dime el primer número: "))
    numero2 = int(input("Dime el segundo número: "))
    resultado = dividir(numero1, numero2)
    print("*** El resultado es: ", resultado)
    
  if opcion_seleccionada == 5:
    print("******* SUMA AVANZADA *******")
    lista = []
    run = True
    
    while run:
      respuesta = input("Dime el número que deseas sumar (Presiona Q para terminar la suma): ")
      if respuesta.lower() == "q":
        run = False
        resultado = suma_avanzada(lista)
        print("*** El resultado es: ", resultado)
        print("")
      else:  
        lista.append(int(respuesta))
        #print("OK")
        #print(lista)   
