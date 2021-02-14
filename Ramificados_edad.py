def run():
    print('Primera persona.')
    name_uno = input('Ingresa tu nombre: ')
    age_uno = int(input('Ingresa tu edad: '))
    print('Segunda persona.')
    name_dos = input('Ingresa tu nombre: ')
    age_dos = int(input('Ingresa tu edad: '))
    if age_uno > age_dos:
        print(f'{name_uno} es mayor que {name_dos}')
    elif age_uno < age_dos:
        print(f'{name_dos} es mayor que {name_uno}')
    else:
        print(f'{name_uno} tiene la misma edad que {name_dos}')


if __name__ == '__main__':
    run()