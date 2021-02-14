def factorial(n):
    """
    Calcula el factorial de n 
    n entero mayor que cero
    returns n factorial
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n-1)


def run():
    n = int(input("Escribe un entero: "))
    print(f'El factorial de {n} es {factorial(n)}')


if __name__ == '__main__':
    run()