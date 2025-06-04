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

def main():
    nivel_actual = 0 
    
    axel = Personaje(
        "Axel",
        "assets/personaje1.png",
        generar_pos_jugador(),
        {
           'izq':pygame.K_a,
           'der':pygame.K_d,
           'arr':pygame.K_w,
           'aba':pygame.K_s 
        }
    )
    
    dante = Personaje(
        "Dante",
        "assets/personaje2.png",
        generar_pos_jugador(),
        {
           'izq':pygame.K_LEFT,
           'der':pygame.K_RIGHT,
           'arr':pygame.K_UP,
           'aba':pygame.K_DOWN
        }
    )
    
    while True:
        dt = RELOJ.tick(FPS) / 1000.0 
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    nivel_actual = siguiente_nivel(nivel_actual)
                    axel = Personaje(
                        "Axel",
                        "assets/personaje1.png",
                        generar_pos_jugador(),
                        axel.controles
                    )
                    dante = Personaje(
                        "Dante",
                        "assets/personaje2.png",
                        generar_pos_jugador(),
                        dante.controles
                    )
                    print(f"Cambiando a nivel {nivel_actual}: {obtener_nombre_nivel(nivel_actual)}")
                
        teclas = pygame.key.get_pressed()
        axel.actualizar(dt,teclas)
        dante.actualizar(dt,teclas)

        for personaje in [axel,dante]:
            if personaje.rect.colliderect(META_RECT):
                nivel_actual = siguiente_nivel(nivel_actual)
                axel = Personaje(
                    "Axel",
                    "assets/personaje1.png",
                    generar_pos_jugador(),
                    axel.controles
                )
                dante = Personaje(
                    "Dante",
                    "assets/personaje2.png",
                    generar_pos_jugador(),
                    dante.controles)
                print(f"!{personaje.nombre} alcanzó la meta! Cambiando a nivel{nivel_actual}:{obtener_nombre_nivel(nivel_actual)}")
        
        VENTANA.fill(obtener_color_nivel(nivel_actual))
        
        pygame.draw.rect(VENTANA, COLOR_META,META_RECT)
        
        dibujar_obstaculos(VENTANA)
        dibujar_enemigos(VENTANA)
        dibujar_powerups(VENTANA)
                          
        axel.dibujar(VENTANA)
        dante.dibujar(VENTANA)
        
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