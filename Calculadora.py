import turtle

print("Hola, Bienvenido a la calculadora de Juan, ¿cuál es tu nombre?" )
print( "Después de ingresar tu nombre, presiona Enter")
x=input()
print("¡ Muy bien!", x , "¡vamos a comenzar!")


"""La estradas x y y corresponde al eje x y y que van a servir para comenzar
a dibujar la caluladora"""
turtle.screensize(500, 700)
turtle.bgcolor("Turquoise")
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.fillcolor("Dark Orange")
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()
turtle.penup()

"""el siguiente procedimiento dibuja la pantalla de la calculadora"""


def Pantalla():
    turtle.goto(180, 280)
    turtle.seth(-90)
    turtle.pendown()
    turtle.fillcolor("White")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(360)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(360)
    turtle.end_fill()
    

Pantalla()

"""Dibuja las teclas de la calculadora"""


def Cuadros(posx, posy, texto):

    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()
    turtle.seth(-90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(56)
    turtle.right(90)
    turtle.forward(50)
    turtle.seth(0)
    turtle.forward(56)
    turtle.penup()
    turtle.goto((posx - 29), (posy - 42))
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write(texto, move=False, align="center", font=("Arial", 20, "bold"))
    turtle.pencolor("black")
    

Cuadros(180, 170, "AC")

Cuadros(180, 100, "+")
Cuadros(180, 30, "x")
Cuadros(180, -40, "=")

Cuadros(104, 170, "^2")
Cuadros(104, 100, "-")
Cuadros(104, 30, "/")
Cuadros(104, -40, "0")

Cuadros(28, 170, "%")
Cuadros(28, 100, "3")
Cuadros(28, 30, "6")
Cuadros(28, -40, "9")

Cuadros(-48, 170, "00")
Cuadros(-48, 100, "2")
Cuadros(-48, 30, "5")
Cuadros(-48, -40, "8")

Cuadros(-124, 170, ".")
Cuadros(-124, 100, "1")
Cuadros(-124, 30, "4")
Cuadros(-124, -40, "7")

"""definimos las siguientes variable globales que nos serviran para
realizar las operaciones"""
reinicio = "AC"
operando1 = 0
operando2 = 0
z = ''

operacion = ""
permitir = "true"


print("introduzca operandos")




def Digitos(x):
    """Entrada: x =caracteres que representan digitos"""
    """Lo que va a hacer esta funcion es tomar el parametro introducido
    suendo se llama y escribirlo en la pantalla"""
    global z
    t = z + x
    turtle.penup()
    turtle.goto(-160, 220) 
    turtle.write(t, align="left", font=("Arial", 20, "bold"))
    z = z + x

def SyR(x, y):
    """ Entradas :
    x es igual al simbolo de la operacion que se desea ecribir
    y es igual a la operacion que se realiza, en este caso la funcion se
    llama SyR por que pude ser Suma o Resta"""
    """Lo que hace esta funcion es asignar la entrada x para que la tortuga
    la escriba en la pantalla y asignar la entrada y a la variable global
    operacion que sirve despues para indicar que tipo de operacion se realiza"""
    global operando1
    global z
    global operacion
    if (z == "" and z != x):
        turtle.penup()
        turtle.goto(-160, 220)
        turtle.write(x, align="left", font=("Arial", 20, "bold"))
        z = z + x
    elif (z == x):
        print("introduzca operandos")
    elif (z != ""):
        t = z + x
        Pantalla()
        turtle.penup()
        turtle.goto(170, 250)
        turtle.write(t, align="right", font=("Arial", 15, "bold"))
        operacion = y
        operando1 = int (z)

        z = ""
    

def MyD(x, y):
    
    global operando1
    global z
    global operacion
    if (z == ""):
        print("introduzca operando")
    elif (z != ""):
        t = z + x
        Pantalla()
        turtle.penup()
        turtle.goto(170, 250)
        turtle.write(t, align="right", font=("Arial", 15, "bold"))
        operacion = y
        operando1 = float(z)

        z = ""
def operar(operar):
           pass

def obtenerxy(x, y):
    
    global permitir
    global operando1
    global operando2
    global operacion
    global z
    global reinicio

    # el siguiente es el numeros de digitos permitidos e =22 digitos
    e = 22
    """Lo que hago a continuacion es reiniciar un proceso cuando no se permite algo"""
    if (reinicio == "true"):
        global z
        z = ""
        Pantalla()
        reinicio = "false"
    """ la siguiente es la operacion de elevacion al cuadrado; esta requiere un poco mas
    de cuidado para evitar que se introduzcan mas de una elevacion a la ves. Trabaja con una variable global
    llamada permitir que es la que permite la accion de elevacion al cuadrado o no, dependiendo de que
    se unda despues de indicar la operacion cuadrado activada al undir el simbolo ^2"""
    if (permitir == "false"):
        if (x > 124 and x < 180 and y > -88 and y < -32 and len(z) <= e and operacion == "cuadrado"):
            Pantalla()
            operar(operando1 * operando1)
            permitir = "true"
            z = ""
            operando1 = 0
            operando2 = 0
        else:
            Pantalla()
            z = ""
            print("Solo una elevacion por numero")
            permitir = "true"

    


            # primera fila de cuadros
    if (x > -180 and x < -124 and y > 120 and y < 170 and len(z) < e):
        if (z != "."):
            Digitos(".")
        if (z == ".."):
            reinicio = "true"
    if (x > -104 and x < -48 and y > 120 and y < 170 and len(z) < e):
        Digitos("00")
    # simbolo y proceso de porcentaje
    if (x > -28 and x < 28 and y > 120 and y < 170 and len(z) < e):
        if (z == ""):
            print("introduzca operacion ")
        elif (z != ""):
            t = z + "%"
            Pantalla()
            turtle.penup()
            turtle.goto(170, 250)
            turtle.write(t, align="right", font=("Arial", 15, "bold"))
            operacion = "porcentaje"
            operando1 = float(z)

            z = ""
            # simbolo y proceso elevacion al cuadrado
    if (x > 48 and x < 104 and y > 120 and y < 170 and len(z)):
        if (z == ""):
            print("introduzca operacion")
        elif (z != ""):
            t = z + "^2"
            turtle.penup()
            turtle.goto(-160, 220)
            turtle.write(t, align="left", font=("Arial", 20, "bold"))
            operacion = "cuadrado"
            permitir = "true"
            operando1 = float(z)
            # Proceso borrar todo
    if (x > 124 and x < 180 and y > 120 and y < 170):
        z = ''
        turtle.penup()
        turtle.goto(-160, 220)
        turtle.write(z, align="left", font=("Arial", 20, "bold"))
        Pantalla()
    # segunda fila de cuadros
    # escribir 1
    if (x > -180 and x < -124 and y > 64 and y < 114 and len(z) < e):
        Digitos("1")
    # escribir 2
    if (x > -104 and x < -48 and y > 64 and y < 114 and len(z) < e):
        Digitos("2")
    if (x > -28 and x < 28 and y > 64 and y < 114 and len(z) < e):
        Digitos("3")
    # la siguiente es rl simbolo y proceso de resta
    if (x > 48 and x < 104 and y > 64 and y < 114):
        SyR("-", "resta")
    # la siguientes es el simbolo y proceso de suma
    if (x > 124 and x < 180 and y > 64 and y < 114):
        SyR("+", "suma")
    # tercera lineas de cuadros
    # digitos del 4 al 6
    if (x > -180 and x < -124 and y > -12 and y < 44 and len(z) < e):
        Digitos("4")
    if (x > -104 and x < -48 and y > -12 and y < 44 and len(z) < e):
        Digitos("5")
    if (x > -28 and x < 28 and y > -12 and y < 44 and len(z) < e):
        Digitos("6")
    # simbolo y proceso division
    if (x > 48 and x < 104 and y > -20 and y < 44):
        MyD("/", "division")
    # simbolo y proceso multiplicacion
    if (x > 124 and x < 180 and y > -12 and y < 44):
        MyD("*", "multiplicacion")
    # Cuarta fila de cuadros
    if (x > -180 and x < -124 and y > -88 and y < -32 and len(z) < e):
        Digitos("7")
    if (x > -104 and x < -48 and y > -88 and y < -32 and len(z) < e):
        Digitos("8")
    if (x > -28 and x < 28 and y > -88 and y < -32 and len(z) < e):
        Digitos("9")
    if (x > 48 and x < 104 and y > -88 and y < -32 and len(z) < e):
        Digitos("0")


        """las siguientes condiciones van a realizar las operaciones
    ya determinadas por la escritura del digito guardada en la variable
    global operacion"""
    if (x > 124 and x < 180 and y > -88 and y < -32 and len(z) <= e):
        turtle.penup()
        reinicio = "true"
        if (z == ""):
            print('introduzca operando')
        elif (z != ""):
            operando2 = float(z)
            Pantalla()
            if (operacion == ""):
                Pantalla()
                print("debes ingresar una operacion por lo menos")
            if (operacion == "resta"):
                operar(operando1 - operando2)
                turtle.penup()
                turtle.goto(-160, 220)
                turtle.write(operando1 - operando2, align="left", font=("Arial", 20, "bold"))
            if  (operacion == "suma"):
                operar(operando1 + operando2)
                turtle.penup()
                turtle.goto(-160, 220)
                turtle.write(operando1 + operando2, align="left", font=("Arial", 20, "bold"))
            if (operacion == "division"):
                operar(operando1 / operando2)
                turtle.penup()
                turtle.goto(-160, 220)
                turtle.write(operando1 / operando2, align="left", font=("Arial", 20, "bold"))
            if (operacion == "multiplicacion"):
                operar(operando1 * operando2)
                turtle.penup()
                turtle.goto(-160, 220)
                turtle.write(operando1 * operando2, align="left", font=("Arial", 20, "bold"))
                
            if (operacion == "porcentaje"):

                operar((operando1 * operando2) / 100)
                turtle.penup()
                turtle.goto(-160, 220)
                turtle.write(operando1 * operando2 *1/ 100, align="left", font=("Arial", 20, "bold"))
               
            if (operacion == "cuadrado"):
                operar(operando1 * operando1)
    
                turtle.penup()
                turtle.goto(-160, 220)
                turtle.write(operando1 * operando1 , align="left", font=("Arial", 20, "bold"))
                
             

                
            z = ''
            operando1 = 0
            operando2 = 0

           
                 
            


turtle.onscreenclick(obtenerxy)



