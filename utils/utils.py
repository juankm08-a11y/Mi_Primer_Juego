import random 
from pygame import Rect
from settings.settings import ANCHO,ALTO,META_RECT

def generar_pos_jugador(tamaño=64):
    while True:
        x = random.randint(50,ANCHO -150)
        y = random.randint(50,ALTO-150)
        pos = Rect(x,y,tamaño,tamaño)
        if not pos.colliderect(META_RECT):
            return(x,y)
