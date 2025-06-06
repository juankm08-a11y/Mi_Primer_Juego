import sys 
import pygame
from settings.settings import ANCHO,ALTO,FPS,VENTANA,RELOJ,META_RECT,COLOR_META
from utils.utils import generar_pos_jugador
from niveles.niveles import obtener_color_nivel, obtener_nombre_nivel,siguiente_nivel
from personajes.personajes import Personaje
from elementos.elementos import (
    dibujar_obstaculos,
    dibujar_enemigos,
    dibujar_powerups
)

def seleccionar_personaje():
    font = pygame.font.SysFont(None,48)
    prompt = font.render("1-Axel     2-Dante",True,(255,255,255))
    img1 = pygame.transform.scale(
        pygame.image.load("assets/personaje1.png"),(80,80)
    )
    img2 = pygame.transform.scale(
        pygame.image.load("assets/personaje.png"),(80,80)
    )
    
    while True:
        VENTANA.fill((20,20,20))
        VENTANA.blit(
            prompt,
            (ANCHO//2-prompt.get_width()//2, ALTO//4)
        )
        VENTANA.blit(img1,(ANCHO//3-40,ALTO//2-ALTO))
        VENTANA.blit(img2,(2*ANCHO//3-40,ALTO//2-ALTO))
        pygame.display.flip()
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    return {
                        "nombre":"Axel",
                        "sprite":"assets/personaje1.png",
                        "controles":{
                            'izq':pygame.K_a,
                            'der':pygame.K_d,
                            'arr':pygame.K_w,
                            'aba':pygame.K_s,
                        }
                    }
                if e.key == pygame.K_2:
                    return {
                        "nombre":"Dante",
                        "sprite":"assets/personaje2.png",
                        "controles":{
                            'izq':pygame.K_LEFT,
                            'der':pygame.K_RIGHT,
                            'arr':pygame.K_UP,
                            'aba':pygame.K_DOWN,
                        }
                    }

def main():
    elec = seleccionar_personaje()
    nivel_actual = 0 
    
    jugador = Personaje(
        elec["nombre"],
        elec["sprite"],
        generar_pos_jugador(),
        elec["controles"]
    )
    while True:
        dt = RELOJ.tick(FPS) / 1000.0 
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                nivel_actual = siguiente_nivel(nivel_actual)
                jugador = Personaje(
                        elec["nombre"],
                        elec["sprite"],
                        generar_pos_jugador(),
                        elec["controles"]
                )
                  
                
        teclas = pygame.key.get_pressed()
        jugador.update(dt,teclas)
        
        if jugador.rect.colliderect(META_RECT):
            nivel_actual = siguiente_nivel(nivel_actual)
            print(f"¡{jugador.nombre} alcanzalo la meta y paso al nivel {nivel_actual}:{obtener_nombre_nivel(nivel_actual)}")
            jugador = Personaje(
                        elec["nombre"],
                        elec["sprite"],
                        generar_pos_jugador(),
                        elec["controles"]
            )
        
        VENTANA.fill(obtener_color_nivel(nivel_actual))
        
        pygame.draw.rect(VENTANA, COLOR_META,META_RECT)
        
        dibujar_obstaculos(VENTANA)
        dibujar_enemigos(VENTANA)
        dibujar_powerups(VENTANA)
                          
        jugador.dibujar(VENTANA)
        
        font = pygame.font.SysFont(None, 36)
        texto_nivel = font.render(
            f"Nivel:{obtener_nombre_nivel(nivel_actual)} (Pulsa Enter)",
            True,
            (255,255,255)
        )
        VENTANA.blit(texto_nivel,(10,10))
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()