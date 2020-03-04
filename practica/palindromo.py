# -*- coding: utf-8 -*-

def palindrome(word):
    reverse_letter = []

    for letter in word:
        reverse_letter.insert(0, letter)
    reverse_word = ''.join(reverse_letter)

    if reverse_word == word:
        return True
    return False

def palindrome2(word):
    reverse_word = word[::-1]

    if reverse_word == word:
        return True
    return False

if __name__ == '__main__':
    
    print('Detectar si una palabra es palíndromo')
    word = str(input('Escribe una palabra: '))
    result = palindrome2(word)

    if result is True:
        print('La palabra {} es un palíndromo'.format(word))
    else:
        print('La palabra {} no es palíndromo'.format(word))
