# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    tAndrey = turtle.Turtle()

    make_rectangle(tAndrey)

    window.mainloop()

def make_rectangle(tAndrey):
    length = int(input('Tamaño del cuadrado'))

    for i in range(4):
        make_line_and_turn(tAndrey, length)

def make_line_and_turn(tAndrey, length):
    tAndrey.forward(length)
    tAndrey.left(90)


if __name__ == '__main__':
    main()
