import pygame 
from settings.settings import VENTANA

class SpriteBase(pygame.sprite.Sprite):
    def __init__(self,sprite_sheet_path, frame_width,frame_height,cols,rows,pos,speed=400,anim_time=0.1):
        super().__init__()
        sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        total_w = frame_width * cols
        total_h = frame_height * rows
        sheet = pygame.transform.scale(sheet,(total_w,total_h))
        self.frames = []
        for y in range(rows):
            for x in range(cols):
                rect = pygame.Rect(x*frame_width, y * frame_height, frame_width, frame_height)
                frame = sheet.subsurface(rect)
                self.frames.append(frame)
        
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.anim_time = anim_time
        self.current_time = 0.0
        
    def animate(self,dt):
        self.current_time += dt
        if self.current_time >= self.anim_time:
            self.current_time = 0.0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
        
    def update(self,dt,*args,**kwargs):
        raise NotImplementedError("Subclases must implement update()")
        
class Personaje(SpriteBase):
    def __init__(self,nombre, sprite_path, pos,controles, speed=500, frame_size=(64,64), cols=1, rows=1):
        
        super().__init__(sprite_path, frame_size[0],frame_size[1],cols,rows,pos,speed)
        self.nombre = nombre
        self.controles = controles
    
    def update(self,dt,teclas):
        dx = dy = 0
        moviendo = False
        
        if teclas[self.controles['izq']]:
            dx = -self.speed * dt
            moviendo = True
        if teclas[self.controles['der']]:
            dx = self.speed * dt
            moviendo = True
        if teclas[self.controles['arr']]:
            dy = -self.speed * dt
            moviendo = True
        if teclas[self.controles['aba']]:
            dy = self.speed * dt
            moviendo = True
  
        self.rect.x += dx
        self.rect.y += dy  
        
        self.rect.clamp_ip(VENTANA.get_rect())
        
        if moviendo:
            self.animate(dt)
        else:
            self.frame_index = 0
            self.image = self.frames[0]
            
    def dibujar(self,pantalla):
        pantalla.blit(self.image, self.rect)
        font = pygame.font.SysFont(None,20)
        nombre_txt = font.render(self.nombre, True,(255,255,255))
        pantalla.blit(nombre_txt, (self.rect.x,self.rect.y -20))

