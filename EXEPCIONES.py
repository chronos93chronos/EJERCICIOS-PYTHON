# EJERCICIO DE EXCEPCIONES EN PYTHON 

"""
Ejercicio 1: División por cero

Escribe un código que solicite al usuario dos números y luego divida el primero por el segundo. Maneja la excepción ZeroDivisionError e 
imprime un mensaje informativo si se intenta dividir por cero.
"""

def division():
    
    try:
         num1 = float(input("ingresar valor 1: "))
         num2 = float(input("ingresar valor 2: "))
         resultado = num1/num2
         print(resultado)
    except ZeroDivisionError:
  
         print(f"ERROR FAVOR VOLVER A INGRESAR DATOS")
         division()

 
division()
"""
Ejercicio 2: Acceso a índices fuera de rango

Crea una lista de nombres y luego solicita al usuario un índice. Accede al elemento de la lista en el índice especificado. Maneja la 
excepción IndexError si el índice está fuera de rango e imprime un mensaje informativo.
"""

def busqueda():
    try:
        nombres = ["ale","tomas","ruben","emilia","camila"]
        indice = int(input("favor ingresar indice: "))
        print(nombres[indice])
    except IndexError:
        print("indice no encontrado, favor volver a ingresar")
        busqueda()

busqueda()

"""
Ejercicio 3: Apertura y lectura de archivos

Intenta abrir un archivo de texto, leer su contenido y luego imprimirlo en la consola. Maneja la excepción FileNotFoundError si el 
archivo no existe e imprime un mensaje informativo.
"""

def leer_archivo():
    try:
        nombre_archivo = input("ingresar el nombre del archivo: ")
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    
    except FileNotFoundError:
        print('ERROR, ARCHIVO NO ENCONTRADO, VOLVER A BUSCAR')
        leer_archivo()

leer_archivo()

"""
Ejercicio 4: Conversión de tipos de datos

Convierte una cadena de texto a un número entero. Maneja la excepción ValueError si la cadena no contiene un número válido e 
imprime un mensaje informativo.
"""

def transformacion():
    try:
      cadena = str(input("ingresar cadena: "))
      conversion = int(cadena)
      print(conversion)
      print(type(conversion))
    except ValueError:
      print('ERROR, LA CADENA SOLO ACEPTA NUMEROS')
      transformacion()
    
transformacion()

"""
Ejercicio 5: Validación de entrada de usuario

Solicita al usuario un número entero entre 1 y 100. Valida la entrada y asegúrate de que sea un número entero dentro del rango especificado. 
Maneja las excepciones ValueError e IndexError e imprime mensajes informativos si la entrada no es válida.
"""

def validacion_datos():
    try:
      usuario = int(input("ingresar numero entre 1 y 100: "))
      if 1 <= usuario <= 100:
        print(f"numero ingresado: {usuario}")
      else:
        print(f"¡Error! El número debe estar entre 1 y 100.")
    except ValueError:
      print('ERROR, EL NUMERO DEBE SER UN ENTERO')
      validacion_datos()
    except IndexError:
        print("ERROR EL NUMERO DEBE ESTAR ENTRE 1 Y 100")
        validacion_datos()

validacion_datos()

"""
Ejercicio 1: Calculadora básica

Crea una calculadora básica que permita al usuario realizar operaciones aritméticas básicas (suma, resta, multiplicación y división) 
entre dos números. Maneja las excepciones ValueError y ZeroDivisionError para garantizar que el usuario ingrese números válidos y 
que no se produzcan divisiones por cero.
"""

def calculadora():
    
    try:
        num1 = float(input("ingresar numero 1: "))
        num2 = float(input("ingresar numero 2: "))
        operacion = str(input("favor ingresar operacion (+ - * /): "))
        
        if operacion == "+":
            print(f"RESULTADO: {num1 + num2}")
        elif operacion == "-":
            print(f"RESULTADO: {num1 - num2}")
        elif operacion == "*":
            print(f"RESULTADO: {num1 * num2}")
        elif operacion == "/":
            print(f"RESULTADO: {num1 / num2}")
        else: 
            print("FAVOR INGRESAR UN OPERADOR VALIDO")
            calculadora()
    except ZeroDivisionError:
        print('NO SE PUEDE DIVIDIR POR 0')
    except ValueError:
        print("ERROR, DEBEN SER NUMEROS")
        calculadora()
    
calculadora()

"""
Ejercicio 2: Conversión de unidades

Desarrolla un programa que permita al usuario convertir unidades de temperatura entre Celsius y Fahrenheit. Maneja las excepciones ValueError 
para garantizar que el usuario ingrese un valor numérico válido para la temperatura.
"""

def convertir():
    try:
        celcius = float(input("favor ingresar grados celcius: "))
        Fahrenheit = (celcius * 9/5)+32 
        print(f"celcius: {celcius} a Fahrenheit: {Fahrenheit}") 
    except ValueError:
        print("NUMERO INVALIDO")
        convertir()
    
convertir()

"""
Ejercicio 3: Análisis de texto

Crea un programa que analice un texto ingresado por el usuario y cuente la cantidad de letras, dígitos y espacios en blanco. 
Maneja la excepción IndexError para evitar errores si el usuario no ingresa ningún texto.
""" 

def analizar():
    try:
        usuario = input("favor ingresar cadena: ")
        letras = 0
        digitos = 0
        espacios = 0
        
        for caracter in usuario:
            if caracter.isalpha():
                letras += 1
            elif caracter.isalnum():
                digitos += 1
            elif caracter.isspace():
                espacios += 1
        print(f"LETRAS: {letras}")
        print(f"digitos: {digitos}")
        print(f"espacios: {espacios}")
    except IndexError:
        print("favor ingresar algun dato")
        analizar()

analizar()

""" 
Ejercicio 4: Manejo de archivos

Escribe un programa que abra un archivo de texto, lea su contenido y lo imprima en la consola. Maneja las excepciones FileNotFoundError y 
IOError para garantizar que el archivo exista y se pueda leer correctamente.
""" 
def procesar():
    try:
        usuario = input("ingresar nombre archivo: ")
        with open(usuario, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("ARCHIVO NO ENCONTRADO")
        procesar()
    except IOError:
        print("NO SE PUEDE LEER EL ARCHIVO")
        
procesar()
    
     
 
    
    