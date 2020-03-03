# -*- coding: utf-8 -*-

def run():
    ingresarNumero = int(input('Por favor ingrese el número: '))
    result = is_prime(ingresarNumero)

    if result is True:
        print('El número {} es primo'.format(ingresarNumero))
    else:
        print('El número {} no es primo'.format(ingresarNumero))

def is_prime(ingresarNumero):
    if ingresarNumero < 2:
        return False
    elif ingresarNumero == 2:
        return True
    elif ingresarNumero > 2 and ingresarNumero % 2 == 0:
        return False
    else:
        for i in range(3,ingresarNumero):
            if ingresarNumero % i == 0:
                return False
                
    return True


if __name__ == '__main__':
    run()