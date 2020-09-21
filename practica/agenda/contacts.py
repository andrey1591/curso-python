# -*_ coding: utf-8 -*-

class Contact:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
       
def run():

    contact_book = ContactBook()


    while True:
        command = str(input('''
        ¿Qué deseas hacer?

        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        '''))


        if command == 'a':
            name = str(input('Escribe el nombre del contacto'))
            phone = str(input('Escribe el número de telefono'))
            email = str(input('Escribe el email de contacto'))

            contact_book.add(name, phone, email)
        
        elif command == 'ac':
            print('Actualizar contacto')
        
        elif command == 'b':
            print('Buscar contacto')

        elif command == 'e':
            print('Eliminar contacto')

        elif command == 'l':
            print('Listar contactos')

        elif command == 's':
            break

        else:
            print('Comando no encontrado')



if __name__ == '__main__':
    print('')
    print('---------------MI AGENDA---------------')
    run()