import os

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')

        
def sumar(a:int, b:int)->int:
    """Esta funcion suma dos elementos

    Args:
        a (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: devuelve un numero entero
    """
    return a + b

def restar(a:int, b:int)->int:
    """Esta funcion resta dos elementos

    Args:
        a (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: devuelve un numero entero
    """
    return a - b

def dividir(a:int, b:int)->int:
    """Esta funcion divide dos elementos

    Args:
        a (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: devuelve un numero entero
    """
    if b == 0 or a == 0:
        return "No es posible dividir por cero"
    return a / b

def multiplicar(a:int, b:int)->int:
    """Esta funcion multiplica dos elementos

    Args:
        a (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: devuelve un numero entero
    """
    return a * b

def calc_factorial(a:int, b:int)->int:
    """Esta función devuelve los factoriales de dos números usando otra funcion que los hace por separado

    Args:
        a (int): Primer número entero para calcular su factorial
        b (int): Segundo número entero para calcular su factorial

    Returns:
        int: devuelve dos numeros enteros
    """
    def factorial(n:int)->int:
        """Esta función devuelve el factorial de un numero

        Args:
            n (int): numero entero 

        Returns:
            int: devuelve numero entero
        """
        if n < 0:
            return "Factorial no definido para números negativos"
        if n == 0:
            return 1
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    return factorial(a), factorial(b)
