import pygame 
from settings.settings import VENTANA

class Personaje:
    def __init__(self,nombre, ruta_imagen, pos,controles,velocidad=500,tamaño=(64,64) , ):
        
        self.nombre = nombre
        original = pygame.image.load(ruta_imagen).convert_alpha()
        self.sprite_sheet = pygame.transform.scale(original, tamaño)
        self.frames = self.cargar_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        
        self.velocidad = velocidad
        self.tiempo_animacion = 0.1
        self.tiempo_actual = 0
        
        self.controles = controles
    
    def cargar_frames(self):
        return [self.sprite_sheet]
        
        
    def actualizar(self,dt,teclas):
        dx = dy = 0
        moviendo = False
        
        if teclas[self.controles['izq']]:
            dx = -self.velocidad * dt
            moviendo = True
        if teclas[self.controles['der']]:
            dx = self.velocidad * dt
            moviendo = True
        if teclas[self.controles['arr']]:
            dy = -self.velocidad * dt
            moviendo = True
        if teclas[self.controles['aba']]:
            dy = self.velocidad * dt
            moviendo = True
            
          
        self.rect.x += dx
        self.rect.y += dy  
        
        self.rect.clamp_ip(VENTANA.get_rect())
        
        if moviendo:
            self.tiempo_actual += dt
            if self.tiempo_actual >= self.tiempo_animacion:
                self.tiempo_actual = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
        else:
            self.frame_index = 0
            
        self.image = self.frames[self.frame_index]      
        
        
    
    def dibujar(self,pantalla):
        pantalla.blit(self.image, self.rect)
        font = pygame.font.SysFont(None,20)
        nombre_txt = font.render(self.nombre, True,(255,255,255))
        pantalla.blit(nombre_txt, (self.rect.x,self.rect.y -20))

