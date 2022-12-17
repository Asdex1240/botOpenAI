import os

def verificarCarpeta():
    if not os.path.exists('./media'):
        os.mkdir('./media')
        print('Carpeta media creada')
    else:
        print('Carpeta media ya existe')