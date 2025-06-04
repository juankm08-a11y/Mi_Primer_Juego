import pygame 


obstaculos = [
    pygame.Rect(300,300,50,50)
]

enemigos = [
    pygame.Rect(500,150,40,40)
]

powerups = [
    pygame.Rect(150,400,30,30)
]

def dibujar_obstaculos(pantalla, color=(100,100,100)):
    for obs in obstaculos:
        pygame.draw.rect(pantalla,color,obs)
        
def dibujar_enemigos(pantalla,color=(200,0,0)):
    for enem in enemigos:
        pygame.draw.rect(pantalla,color,enem)

def dibujar_powerups(pantalla,color=(0,255,255)):
    for pu in powerups:
        pygame.draw.rect(pantalla,color,pu)
