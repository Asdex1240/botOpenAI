import pygame

def reproducir(archivo):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue