import random

game_active = bool(True)
dinero = 0

palo_carta = ("Corazones", "Picas", "Diamantes", "Tréboles")

numero_cartas= ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

valor_cartas = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

nombre_jugador = input("Ingrese su nombre de jugador: ")

dinero_usuario = int(input("Ingrese la cantidad de dinero con la que desea comenzar (mínimo $15.000 y máximo $1.000.000): "))

if dinero_usuario < 15000 or dinero_usuario > 1000000:
    print("El dinero inicial debe estar entre $15.000 y $1.000.000.")

# Función calcular_mano recibe un parámetro mano (puede ser mano_jugador o mano_dealer)
def calcular_mano(mano):
    puntos_total = 0
    cantidad_ases = 0

    for carta in mano:
        val = valor_cartas[carta]
        puntos_total = puntos_total + val

        if carta == "A":
            cantidad_ases = cantidad_ases + 1

    while puntos_total > 21 and cantidad_ases > 0:
        puntos_total = puntos_total - 10
        cantidad_ases = cantidad_ases - 1

    return puntos_total


def play_blackjack():
    global dinero_usuario, game_active

    print("Bienvenido al BlackJack SanGa - " + nombre_jugador)

    while game_active:

        if dinero_usuario < 15000:
            print("No tienes suficiente dinero para realizar otra apuesta.")
            break

        print("Dinero disponible: $", dinero_usuario)

        respuesta = input("Ingrese su apuesta con un numero entero entre $15.000 y $1.000.000 o escriba 'salir'):")

        if respuesta == "salir":
            game_active = False
            break

        apuesta = int(respuesta)

        # Apuesta
        if apuesta < 15000:
            print("La apuesta mínima es de $15.000.")
            continue

        if apuesta > 1000000:
            print("La apuesta máxima es de $1.000.000.")
            continue

        if apuesta > dinero_usuario:
            print("No puede apostar más dinero del que tiene disponible.")
            continue

        # Creación y mezcla del mazo (lista)
        mazo = [] # Creación lista vacía

        for palo in palo_carta: # Recorrer 4 veces
            for numero in numero_cartas:
                mazo.append(numero)

        random.shuffle(mazo) # Método shuffle de la librería importada random: mezcla las cartas

        mano_jugador = [mazo.pop(), mazo.pop()] # Llena de cartas cada mano
        mano_dealer = [mazo.pop(), mazo.pop()] # Llena de cartas cada mano

        print("Tu mano:", mano_jugador,
              "Valor:", calcular_mano(mano_jugador))

        # Turno del jugador
        while True:
            choice = input("¿Desea otra carta? (p = pedir, s = plantarse): ")

            if choice == "p":
                mano_jugador.append(mazo.pop())

                p_val = calcular_mano(mano_jugador)

                print("Mano:", mano_jugador, "Valor:", p_val)

                if p_val > 21:
                    print("¡Te pasaste de 21! Perdiste la mano.")
                    dinero_usuario = dinero_usuario - apuesta
                    break

            elif choice == "s":
                break

            else:
                print("Opción inválida, intente nuevamente.")

        # Turno del dealer
        if calcular_mano(mano_jugador) <= 21:

            d_val = calcular_mano(mano_dealer)

            while d_val < 17:
                mano_dealer.append(mazo.pop())
                d_val = calcular_mano(mano_dealer)

            print("Mano del dealer:", mano_dealer, "Valor:", d_val)

            p_val = calcular_mano(mano_jugador)

            # Resultado de la ronda
            if (p_val > d_val or d_val > 21) and not (p_val > 21):
                print("¡Ganaste la ronda!")
                dinero_usuario = dinero_usuario + apuesta
            elif p_val == d_val:
                print("Empate en la ronda.")
            else:
                print("El dealer gana.")
                dinero_usuario = dinero_usuario - apuesta

        print("Dinero disponible después de la ronda: $", dinero_usuario)

    print("Fin del juego. Dinero final: $", dinero_usuario)

# Inicio del programa
play_blackjack()