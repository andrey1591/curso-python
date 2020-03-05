# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'avion',
    'carro',
    'telefono',
    'lenovo',
    'moto',
    'celular',
    'pollo'
]

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def display_board(hidden_word,trieds):
    print(IMAGES[trieds])
    print('')
    print(hidden_word)
    print('')
    print('--- * --- * --- * --- * --- * --- ')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    trieds = 0

    while True:
        display_board(hidden_word,trieds)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            trieds += 1

            if trieds == 7:
                display_board(hidden_word, trieds)
                print('')
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break


if __name__ == '__main__':

    print(' B I E N V E N I D O   A   A H O R C A D O S ')
    run()