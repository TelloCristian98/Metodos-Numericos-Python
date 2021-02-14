def aproximacion(objetivo):    
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def busqueda_binaria(objetivo):    
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def enumeracion(objetivo):    
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')    



def run():
    print("""Bienvenido a métodos numéricos. 
    Escoge un método para resolver raiz cuadrada
    1. Aproximacion
    2. Búsqueda Binaria
    3. Enumeración""")
    opcion = int(input('Escoge una opción: '))
    if opcion > 0 and opcion < 4:
        objetivo = int(input('¿A qué número quieres sacarle la raiz? : '))

    if opcion == 1:        
        aproximacion(objetivo)
    elif opcion == 2:        
        busqueda_binaria(objetivo)
    elif opcion == 3:        
        enumeracion(objetivo)
    else:
        print('Opción no valida')



if __name__ == '__main__':
    run()