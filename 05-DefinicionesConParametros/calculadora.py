# -*- coding: utf-8 -*-

def run():
    print('---------- C A L C U L A D O R A ----------')
    print('Convierte pesos Colombiamos a Dolares')
    print('Cuanto dinero quieres convertir?')
    print('')


    dinero = float(input('ingresa la cantidad de Dinero '))

    resultado = calcular(dinero)

    print('${} Pesos Colombianos en Dolares son: ${} '.format(dinero, resultado))
    

def calcular(dinero):
    preciDola = int(3500)
    return dinero / preciDola



if __name__ == '__main__':
    run() 