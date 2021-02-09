#Kevin Ricardo caballero Cepeda, 1932995

velocidad=80 #Variable conocida 1
presupuesto=500 #Variable conocida 2

rendimiento_variable=float(input("Rendimiento: ")) #Solicitamos Variable 3
gasolina_precio_litro=float(input("Precio por litro: ")) #Solciitamos Variable 4

if rendimiento_variable<=0:
    print("Ingresó un valor inválido")
else:
    if gasolina_precio_litro<=0:
        print("Ingresó un valor inválido")
    else:     

        litros_gasolinas=presupuesto/gasolina_precio_litro #Operación 1
        distancia=litros_gasolinas*rendimiento_variable #Operación 2
        tiempo_decimal=distancia/velocidad #Operación 3
        horas=int(tiempo_decimal) #Operación 4
        minutos=int((tiempo_decimal-horas)*60) #Operación 4

        print("-------\nCon $",presupuesto,"pesos")
        print("se recorren",distancia,"Km")
        print("en ",horas," horas",minutos,"minutos.\n-------")