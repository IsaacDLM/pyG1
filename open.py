continuar = True
while continuar:
    print("MENU")
    print("1. Ejercicio uno")
    print("2. Ejercicio Dos")
    print("3. Salir")
    opcion = int(input("Elija una opcion: "))


    match opcion:
        #ejercicio 1
        case 1:
            a = float(input("ingrese el valor de 'a' :" )) #si no nombramos el tipo de dato
            b = float(input("ingrese el valor de 'b' :" )) #Python interpreta que es un str
            c = float(input("ingrese el valor de 'c' :" ))

            respuestaUno = ( a * (a * a)) * ((b * b) - 2 *(a * c)) / (2 * b) #esta es la forma larga
            respuestaUno = ( a**3 ) * ( b**2 - 2*a*c ) / ( 2 * b ) #esta es la forma optima

            print(f"la respuesta es:  {respuestaUno}""\n")
        case 2:
            #ejercicio 2
            y = float(input("ingrese el valor de 'y': "))
            z = float(input("ingrese el valor de 'z': "))

            respuestaDos = ((3 + 5 * 8)< 3 ) and ((-6/3 * 4) + 2<2) or (y > z) 

            print(f"La respuesta es: {respuestaDos}""\n")
        case 3:
            print("\n""Adios!!!""\n")
            continuar = False    
        case _:
            print("\n""opcion invalida""\n")        
    