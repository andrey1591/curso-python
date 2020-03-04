# -*- coding: utf-8 -*-
import random


def run():
    
    numero_random = random.randint(0, 20)
    numero_cond = False

    while not  numero_cond:
        numero = int(input('Adivina el número: '))
        if numero == numero_random: 
            print('Felicidades')
            numero_cond = True
        elif numero > numero_random:
            print('El número debe ser menor')
        else:
            print('El número debe ser mayor')




if __name__ == '__main__':
    run()