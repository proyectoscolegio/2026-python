ubicaciones = {}
cantidad_ubicaciones = 0

#Funcion input que chequea que el valor sea un número entero útil.-
#Es como un input normal, pero solo admite INT.
def input_int(valor):
    valor_ingresado_correcto = False
    while valor_ingresado_correcto == False:    
        try:
            dato_ingresado = int(input(valor))
        except:
            print(f"\nEL VALOR INGRESADO DEBE SER UN NUMERO ENTERO")
        else:
            valor_ingresado_correcto = True
    return dato_ingresado


#Imprime el menú principal con las ubicaciones.
def main_menu():
    print(f"\n-------------------")
    print(f"| USTED ESTÁ AQUI |")
    print(f"-------------------")
    
    if len(ubicaciones) == 0:  #Chequea si hay algo en el diccionario y avisa si no hay nada.
        print(" <Sin ubicaciones>") 
    else:
        print("  |")

    for i in ubicaciones:   #Genera el espacio para imprimir las ubicaciones.
        print("  |")
        print(i,end="")
        print(" |",end="")
        for j in range(int(ubicaciones[i]["distancia"]/100)): #Grafica distancia con un guión por cada 100 metros.
            print("-",end="")
        print(f"{ubicaciones[i]["nombre"]} ({ubicaciones[i]["distancia"]}mts)") #Imprime nombre y distancia de la ubicacion despues de la linea.

    print(f"\n1-Agregar una ubicación")
    if not len(ubicaciones) == 0: #Solo se imprime si hay ubicaciones almacenadas.
        print("2-Ir a una ubicación")


#Funcion que almacena las ubicaciones en un diccionario.
def agregar_ubicacion():
    global cantidad_ubicaciones
    cantidad_ubicaciones += 1  #Aumenta cantidad de ubicaciones por cada una que se agrega.
    
    n = input("Ingrese el nombre de la ubicacion: ")
    while n.strip() == "":       #"strip()" Elimina los espacios antes de chequear si no hay texto ingresado.
        print("EL NOMBRE NO PUEDE ESTAR VACÍO")
        n = input("Ingrese el nombre de la ubicacion: ")

    d = input_int("Ingrese la distancia de la ubicacion en cuadras (x100 metros): ")
    while d < 1 or d > 300: #Chequea que la distancia sea mayor a 1
        print("LA DISTANCIA DEBE SER ENTRE 1 Y 300 CUADRAS (0,1-30Km)")
        d = input_int("Ingrese la distancia de la ubicacion en cuadras (x100 metros): ")

    d*=100 #Convierte "d" de cuadras a metros para almacenarlo.
    ubicaciones[cantidad_ubicaciones] = {"nombre":n, "distancia":d} #Agrega la informacion de la ubicacion en el siguiente item.

    main_menu()


#Elección de destino y cálculo de tiempo según distancia y velocidad.
def destino():
    destino = input_int("Ingrese el número de su destino: ")
    while destino > cantidad_ubicaciones or destino < 1:   #Chequea que el numero de destino ingresado exista.
        print("NUMERO DE UBICACIÓN INEXISTENTE")
        destino = input_int("Ingrese el número de su destino: ")
        
    print(f"\n1-Auto (40km/h) | 2-A pie (5km/h) | 3-Bus (50km/h) | 4-Bicicleta (15km/h) | 5-Otro (ingresar velocidad)") #Opciones
    metodo = input_int("¿Cómo desea viajar?: ")
    while metodo < 1 or metodo > 5: #Comprueba que el metodo seleccionado existe o pregunta de nuevo.
        print("METODO DE TRANSPORTE INEXISTENTE")
        metodo = input_int("¿Cómo desea viajar?: ")

    #Cálculo de tiempo según distancia y metodo de transporte.
    if metodo == 5: #Este if está separado para que no interfiera en la interfaz de abajo.
        velocidad_kmh = input_int("Indique la velocidad que va a ir (km/h): ")  #km/h
        while velocidad_kmh < 1:
            print("INGRESE UNA VELOCIDAD MAYOR A UNO")
            velocidad_kmh = input_int("Indique a la velocidad que va a viajar (km/h): ")
    print(f"\n--------------------------------------------------------------------")
    print("  ", end="")
    if metodo == 1: #AUTO
        medio = "en auto"
        velocidad_kmh = 40  #km/h
    elif metodo == 2: #A PIE
        medio = "a pie"
        velocidad_kmh = 5  #km/h
    elif metodo == 3: #BUS
        medio = "en bus"
        velocidad_kmh = 50  #km/h
    elif metodo == 4 : #BICICLETA
        medio = "en bicicleta"
        velocidad_kmh = 15  #km/h
    elif metodo == 5 : #PERSONALIZADO
        medio = f"a {velocidad_kmh}km/h"
    distancia_destino = ubicaciones[destino]["distancia"]
    nombre_destino = ubicaciones[destino]["nombre"]
    tiempo_minutos = (distancia_destino/(velocidad_kmh/3.6))/60 #Cálculo de tiempo.
    print(f"Usted tardará {tiempo_minutos:.2f} minutos en llegar a {nombre_destino} ({distancia_destino}m) {medio}.")
    print(f"--------------------------------------------------------------------\n")


#Introducción antes del bucle
print(f"\n-----------------------------------------------")
print("              Bienvenido a SUP")
print(f"        Sistema de Ubicación Personal")
print(f"-----------------------------------------------")
print(f" Ingrese sus ubicaciones para guiar su camino. ")
print(f"       Cada ( - ) representa 100 metros.")
print(f"----------------------------------------------- \n")
main_menu()

ejecutar = True #Mientras este valor sea True, el programa estará ejecutandose.
############################LOOP###############################
while ejecutar: #Bucle
    while True: #Chequea que la opción ingresada exista
        opcion = input_int("Seleccione una opción: ")
        if opcion == 1 or (opcion == 2 and len(ubicaciones) > 0):
            break
        else: 
            print("OPCIÓN INEXISTENTE")
    
    #Funcion según elección del usuario.
    if opcion == 1:
        agregar_ubicacion()
    elif opcion == 2 and len(ubicaciones) > 0: #Solo ejecuta la opcion 2 si hay ubicaciones.
        destino()
        print("¿Quiere viajar a otra ubicación?")
        while True:
            finalizar = input_int(f"\n1-Sí 2-No: ") #Si el usuario ingresa 2, termina el programa.
            if finalizar == 1:
                main_menu()
                break
            elif finalizar == 2:
                ejecutar = False #Desactiva el bucle.
                print(f"\nGracias por viajar con SUP. ¡Que tenga buen viaje!")
                break
                
            else:
                print("OPCION NO VALIDA.")