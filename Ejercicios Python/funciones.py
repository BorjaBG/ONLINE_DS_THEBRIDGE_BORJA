import math

def convertir_numeros(num: int):
    '''
        Funcion para convertir un numero en el dia de la semana.
        Args:
            num (int): Numero del dia de la semana
        Return:
            str: Dia de la semana
    '''
    match num:
        case 1:
            return "Lunes"
        case 2:
            return "Martes"
        case 3:
            return "Miercoles"
        case 4:
            return "Jueves"
        case 5:
            return "Viernes"
        case 6:
            return "Sabado"
        case 7:
            return "Domingo"
        case _:
            return "¡Error! Ese numero de la semana no es válido"

def piramide(lista_piramide: list):
    '''
        Funcion para imprimir una piramide de numeros.
        Args:
            lista_piramide (list): Lista de numeros para imprimir en forma de piramide.
        Returns:
            None
    '''
    lista_impresa = ""
    imprimir = True

    while imprimir:
        for num in lista_piramide:
            lista_impresa = lista_impresa + f" {str(num)}"
        print(f"{lista_impresa}\n")
        lista_piramide.pop(0)
        lista_impresa = ""

        if len(lista_piramide) == 0:
            imprimir = False

def comparar_numeros(num1: float, num2: float):
    '''
        Funcion para comparar dos numeros.
        Args:
            num1 (float): Primer numero a comparar.
            num2 (float): Segundo numero a comparar.
        Returns:
            None
    '''
    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num2 > num1:
        print(f"{num2} es mayor que {num1}")
    else:
        print(f"{num1} y {num2} son iguales")

def contar_letras(texto: str, letra_buscar: str):
    '''
        Funcion para contar cuantas veces aparece una letra en un texto.
        Args:
            texto (str): Texto en el que se buscará la letra.
            letra_buscar (str): Letra a contar.
        Returns:
            int: Número de veces que aparece la letra en el texto.
    '''
    letra_mayuscula = 0
    letra_minuscula = 0
    for letra in texto:
        if letra == letra_buscar.lower():
            letra_minuscula += 1
        elif letra == letra_buscar.upper():
            letra_mayuscula += 1
    resultado = letra_mayuscula + letra_minuscula
    return resultado

def contar(frase: str):
    '''
        Funcion para contar cuantas veces aparece cada letra en una frase.
        Args:
            frase (str): Frase en la que se contarán las letras.
        Returns:
            dict: Diccionario con las letras como claves y su cantidad como valores.
    '''
    dic_letras = {}

    for letra in frase:
        if letra not in dic_letras:
            dic_letras[letra] = 1
        else:
            dic_letras[letra] = dic_letras[letra] + 1

    return dic_letras

def modificar_elemento(lista: list, comando: str, elemento = None):
    '''
        Funcion para modificar una lista añadiendo o eliminando un elemento.
        Args:
            lista (list): Lista a modificar.
            comando (str): Comando a ejecutar ("add" o "remove").
            elemento (any): Elemento a añadir o eliminar.
        Returns:
            list: Lista modificada.
    '''
    match comando.lower():
        case "add":
            lista.append(elemento)
            return lista
        case "remove":
            lista.remove(elemento)
            return lista

def crear_frase(lista: list):
    '''
        Funcion para crear una frase a partir de una lista de palabras.
        Args:
            lista (list): Lista de palabras.
        Returns:
            str: Frase creada a partir de la lista de palabras.
    '''
    frase = ""

    for palabra in lista:
        frase = frase + " " + palabra
    return frase

def fibonacci(num: int):
    '''
        Funcion para calcular el numero de fibonacci en la posicion indicada.
        Args:
            num (int): Posicion del numero de fibonacci a calcular.
        Returns:
            int: Numero de fibonacci en la posicion indicada.
    '''
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def area_cuadrado(lado: float):
    '''
        Funcion para calcular el area de un cuadrado.
        Args:
            lado (float): Longitud del lado del cuadrado.
        Returns:
            float: Area del cuadrado.
    '''
    area = lado**2
    return area

def area_triangulo(base: float, altura: float):
    '''
        Funcion para calcular el area de un triangulo.
        Args:
            base (float): Longitud de la base del triangulo.
            altura (float): Longitud de la altura del triangulo.
        Returns:
            float: Area del triangulo.
    '''
    area = (base * altura) / 2
    return area

def area_circulo(radio: float):
    '''
        Funcion para calcular el area de un circulo.
        Args:
            radio (float): Longitud del radio del circulo.
        Returns:
            float: Area del circulo.
    '''
    area = math.pi * (radio**2)
    return area

