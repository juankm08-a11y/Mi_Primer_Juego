import pygame 

pygame.init()

ANCHO, ALTO = 800,600 

FPS = 60

META_RECT = pygame.Rect(ANCHO - 100,  ALTO //  2 -25, 60,60)

COLOR_META = (255,215,0)

COLOR_OBSTACULO = (100,100,100)

COLOR_ENEMIGO = (200,0,0)

COLOR_POWERUP = (0,255,255)

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
RELOJ = pygame.time.Clock()