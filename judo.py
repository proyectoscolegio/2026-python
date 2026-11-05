import tkinter as tk , webbrowser 
botones=[]
ventana=tk.Tk()

ventana.title("cinturones de judo")

usuario=input("Ingrese su usuario")

contraseña=int(input("Ingrese su contraseña numerica (proba:86) "))

opcion=input("Ingrese como quiere navegar en la pagina (ventana / elegir / secreto)")

subtitulo=tk.Label(ventana,text="Cinturones de judo", fg="black", bg="white")

subtitulo.pack()

# permite abrir las paginas con info mas detallada
def abrir_enlace():
    webbrowser.open("https://www.judoedu.com.ar/programas-de-ex%C3%A1men?")

def abrir_enlace2():
    webbrowser.open("https://learning.judocanada.org/grading-2/?")

def abrir_enlace3():
    webbrowser.open("https://www.thejudoacademy.com/grading?")

def abrir_enlace4():
    webbrowser.open("https://www.ijf.org/ijf/documents/16?")

def nueva_ventana():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("blanco")
    nueva_ventana.geometry("400x400")
    texto=tk.Label(nueva_ventana,text="Cinturón Blanco — Principiante.Es el primer nivel del judoka.Se aprenden las bases del deporte: posiciones, desplazamientos, caídas y técnicas sencillas.Se aprende:Ukemi: técnicas de caída.Posiciones y desplazamientos.Primeras proyecciones.Normas básicas de seguridad y respeto.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana2():
    nueva_ventana2 = tk.Toplevel(ventana)
    nueva_ventana2.title("amarillo")
    nueva_ventana2.geometry("400x400")
    texto2=tk.Label(nueva_ventana2,text="Cinturón Amarillo — Principiante avanzadoEl judoka empieza a mejorar las técnicas básicas y a combinarlas durante la práctica.Se aprende:Perfeccionamiento de las caídas.Nuevas proyecciones.Técnicas básicas de inmovilización.Mejor utilización del agarre.Combinaciones sencillas de técnicas.Mayor control durante el combate.",fg="black",wraplength=400, padx=0,pady=100,)
    texto2.pack()

def nueva_ventana3():
    nueva_ventana3 = tk.Toplevel(ventana)
    nueva_ventana3.title("naranja")
    nueva_ventana3.geometry("400x400")
    texto=tk.Label(nueva_ventana3,text="Cinturón Naranja — IntermedioSe comienza a desarrollar una mayor variedad de técnicas y a entender cómo utilizarlas según los movimientos del rival.Se aprende:Nuevas técnicas de proyección.Inmovilizaciones más avanzadas.Combinaciones y encadenamientos.Ataques aprovechando el movimiento del oponente.Mejor control del equilibrio.Aplicación de técnicas en randori (práctica de combate).",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana4():
    nueva_ventana4 = tk.Toplevel(ventana)
    nueva_ventana4.title("verde")
    nueva_ventana4.geometry("400x400")
    texto=tk.Label(nueva_ventana4,text="Cinturón Verde — Intermedio avanzadoEl judoka ya tiene una base sólida y empieza a utilizar las técnicas de manera más estratégica.Se aprende:Perfeccionamiento de las proyecciones.Técnicas de suelo más variadas.Combinaciones y contraataques.Mejor manejo del equilibrio y la distancia.Estrategias básicas de combate.Mayor precisión y velocidad.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana5():
    nueva_ventana5 = tk.Toplevel(ventana)
    nueva_ventana5.title("azul")
    nueva_ventana5.geometry("400x400")
    texto=tk.Label(nueva_ventana5,text="Cinturón Azul — AvanzadoSe busca que el judoka pueda aplicar sus conocimientos de forma más completa y adaptarse a diferentes rivales.Se aprende:Técnicas de proyección más complejas.Combinaciones avanzadas.Contraataques.Técnicas de suelo y transiciones.Estrategias de combate.Mayor dominio técnico y táctico.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana6():
    nueva_ventana6 = tk.Toplevel(ventana)
    nueva_ventana6.title("marron")
    nueva_ventana6.geometry("400x400")
    texto=tk.Label(nueva_ventana6,text="Cinturón Marrón — Avanzado superiorEs el último nivel antes del cinturón negro. Se exige un dominio bastante completo de las técnicas del judo.Se aprende:Perfeccionamiento de las técnicas anteriores.Combinaciones y contraataques complejos.Mayor dominio del combate de pie y de suelo.Estrategias avanzadas.Precisión, control y eficacia.Preparación para el examen de cinturón negro.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana7():
    nueva_ventana7 = tk.Toplevel(ventana)
    nueva_ventana7.title("negro")
    nueva_ventana7.geometry("400x400")
    texto=tk.Label(nueva_ventana7,text="Cinturón Negro — DanRepresenta que el judoka alcanzó un alto nivel técnico y que conoce profundamente los fundamentos del judo. No significa que haya terminado de aprender, sino que comienza una etapa de mayor profundización.Se desarrolla:Dominio de las técnicas de judo.Aplicación técnica y estratégica.Kata (formas tradicionales).Enseñanza y transmisión de conocimientos.Disciplina y responsabilidad.Comprensión más profunda de los principios del judo.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana8():
    nueva_ventana8 = tk.Toplevel(ventana)
    nueva_ventana8.title("rojo/blanco")
    nueva_ventana8.geometry("400x400")
    texto=tk.Label(nueva_ventana8,text="Cinturón Rojo y Blanco — Danes superioresSe utiliza en grados superiores del cinturón negro y representa una gran experiencia y trayectoria dentro del judo.Se destaca:Profundo conocimiento técnico.Dominio de las diferentes áreas del judo.Enseñanza y formación de otros judokas.Experiencia y liderazgo.Conservación y transmisión de los valores del judo.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana9():
    nueva_ventana9 = tk.Toplevel(ventana)
    nueva_ventana9.title("rojo")
    nueva_ventana9.geometry("400x400")
    texto=tk.Label(nueva_ventana9,text="Cinturón Rojo — Danes muy superioresEs una de las graduaciones más altas del judo y está reservada para maestros con una trayectoria excepcional.Se caracteriza por:Gran experiencia y conocimiento del judo.Aporte al desarrollo y difusión del deporte.Enseñanza a generaciones de judokas.Ejemplo de disciplina, respeto y valores.Reconocimiento por una trayectoria destacada.",fg="black",wraplength=400, padx=0,pady=100,)
    texto.pack()

def nueva_ventana10():
    nueva_ventana10 = tk.Toplevel(ventana)
    nueva_ventana10.title("Links")
    nueva_ventana10.geometry("400x400")
    boton_enlace1=tk.Button(nueva_ventana10,text="link1",command=abrir_enlace, fg="white", bg="black")
    boton_enlace2=tk.Button(nueva_ventana10,text="link2",command=abrir_enlace2, fg="white", bg="black")
    boton_enlace3=tk.Button(nueva_ventana10,text="link3",command=abrir_enlace3, fg="white", bg="black")
    boton_enlace4=tk.Button(nueva_ventana10,text="link4",command=abrir_enlace4, fg="white", bg="black")
    boton_enlace1.pack()
    boton_enlace2.pack()
    boton_enlace3.pack()
    boton_enlace4.pack()


#permite abrir nuevas ventanas con informacion
if opcion == "ventana":
    ventana


elif opcion == "elegir":
    print("blanco, amarillo, naranja, verde, azul, marron, negro, rojo/blanco o rojo. Para terminar el programa, ingrese salir")
    while True:
        cinturon=input("Elija el cinturón específico que desea ver:")

        if cinturon == "salir":
            break
        elif cinturon == "blanco":
            nueva_ventana()
            botones.append("blanco")
        elif cinturon == "amarillo":
            nueva_ventana2()
            botones.append("amarillo")
        elif cinturon == "naranja":
            nueva_ventana3()
            botones.append("naranja")
        elif cinturon == "verde":
            nueva_ventana4()
            botones.append("verde")
        elif cinturon == "azul":
            nueva_ventana5()
            botones.append("azul")
        elif cinturon == "marron":
            nueva_ventana6()
            botones.append("marron")
        elif cinturon == "negro":
            nueva_ventana7()
            botones.append("negro")
        elif cinturon == "rojo/blanco":
            nueva_ventana8()
            botones.append("rojo/blanco")
        elif cinturon == "rojo":
            nueva_ventana9()
            botones.append("rojo")
        else:
            print("Ese cinturón no existe. Intente nuevamente.")
        print(f"Su historial tiene {len(botones)} botones:")
        for p in botones:
            print(p)

elif opcion == "secreto" and contraseña == 86:
    print("caiste")
else:
    print("eso no es una opcion : se activo la ventana autamaticamente")


#es el tamaño de la ventana principal
ventana.geometry("300x300")

#crea los botones que llevan a las ventanas
boton=tk.Button(ventana,text="links",command=nueva_ventana10, fg="white", bg="black")

boton1=tk.Button(ventana,text="blanco",command=nueva_ventana, fg="black", bg="white")

boton2=tk.Button(ventana,text="amarillo",command=nueva_ventana2, fg="black", bg="yellow")

boton3=tk.Button(ventana,text="naranja",command=nueva_ventana3, fg="black", bg="orange")

boton4=tk.Button(ventana,text="verde",command=nueva_ventana4, fg="black", bg="green")

boton5=tk.Button(ventana,text="azul",command=nueva_ventana5, fg="black", bg="blue")

boton6=tk.Button(ventana,text="marron",command=nueva_ventana6, fg="black", bg="brown")

boton7=tk.Button(ventana,text="negro",command=nueva_ventana7, fg="white", bg="black")

boton8=tk.Button(ventana,text="rojo/blanco",command=nueva_ventana8, fg="white", bg="red")

boton9=tk.Button(ventana,text="rojo",command=nueva_ventana9, fg="black", bg="red")

boton10=tk.Button(ventana)

boton.pack()

boton1.pack()

boton2.pack()

boton3.pack()

boton4.pack()

boton5.pack()

boton6.pack()

boton7.pack()

boton8.pack()

boton9.pack()

ventana.mainloop()