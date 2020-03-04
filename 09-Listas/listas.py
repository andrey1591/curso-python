# -*- coding: utf-8 -*-

def temps_average(temps_list):

    add_temps = 0

    for temp in temps_list:
        add_temps += temp
    return add_temps / len(temps_list)



if __name__ == '__main__':
    temps_list = [26,20,19,22,20,22]

    result = temps_average(temps_list)

    print('La temperatura promedio es {}'.format(result))