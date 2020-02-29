# -*- coding: utf-8 -*-

def run():
    print('-----CALCULADORA DE DIVISAS-----')
    print('')
    print('Calcula pesos colombianos a Dolares')
    print('¿Cuanto dinero quieres convertir?')
    print('')

    pesosColombianos = float(input('Ingrese la cantidad de dinero: '))

    resultado = calcular(pesosColombianos)
    print('${} Pesos Colombianos en Dolares son ${}'.format(pesosColombianos,resultado))


def calcular(pesosColombianos):
    precioDolar = 3500
    return pesosColombianos / precioDolar



if __name__ == '__main__':
    run() 