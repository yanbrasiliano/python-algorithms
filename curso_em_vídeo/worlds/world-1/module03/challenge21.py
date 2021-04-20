import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('/home/hiyan/Documents/GitHub/python-curso-em-video/worlds/world-1/module03/exe21.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
x = input('digite algo para encerrar ...')