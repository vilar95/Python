#Faça um programa em python que abra e reproduza o audio de uma arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('Desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Consegue ouvir?')