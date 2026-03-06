import pygame
import random
import sys
#py -3.13 viborita.py
#para ejecutar usar ese 
# Inicializar pygame
pygame.init()

# ----- CONFIGURACION -----
ANCHO = 600
ALTO = 400
TAM_CUADRADO = 20
FPS = 10

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Vibora")

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 35)

# ----- FUNCIONES -----

def dibujar_snake(lista_snake):
    for bloque in lista_snake:
        pygame.draw.rect(pantalla, VERDE, [bloque[0], bloque[1], TAM_CUADRADO, TAM_CUADRADO])

def mostrar_puntaje(puntaje):
    texto = fuente.render("Puntaje: " + str(puntaje), True, BLANCO)
    pantalla.blit(texto, [10, 10])

def mensaje_game_over():
    texto = fuente.render("GAME OVER - C para continuar o Q para salir", True, BLANCO)
    pantalla.blit(texto, [ANCHO / 10,ALTO / 2 ])
    pygame.display.update()

# ----- JUEGO -----

def juego():
    game_over = False
    cerrar_juego = False

    x = ANCHO / 2
    y = ALTO / 2

    cambio_x = 0
    cambio_y = 0

    snake_lista = []
    snake_longitud = 1

    comida_x = round(random.randrange(0, ANCHO - TAM_CUADRADO) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTO - TAM_CUADRADO) / 20.0) * 20.0

    while not cerrar_juego:

        while game_over:
            pantalla.fill(NEGRO)
            mensaje_game_over()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    cerrar_juego = True
                    game_over = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        cerrar_juego = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    cambio_x = -TAM_CUADRADO
                    cambio_y = 0
                elif evento.key == pygame.K_RIGHT:
                    cambio_x = TAM_CUADRADO
                    cambio_y = 0
                elif evento.key == pygame.K_UP:
                    cambio_y = -TAM_CUADRADO
                    cambio_x = 0
                elif evento.key == pygame.K_DOWN:
                    cambio_y = TAM_CUADRADO
                    cambio_x = 0

        if x >= ANCHO or x < 0 or y >= ALTO or y < 0:
            game_over = True

        x += cambio_x
        y += cambio_y
        pantalla.fill(NEGRO)

        pygame.draw.rect(pantalla, ROJO, [comida_x, comida_y, TAM_CUADRADO, TAM_CUADRADO])

        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        snake_lista.append(cabeza)

        if len(snake_lista) > snake_longitud:
            del snake_lista[0]

        for bloque in snake_lista[:-1]:
            if bloque == cabeza:
                game_over = True

        dibujar_snake(snake_lista)
        mostrar_puntaje(snake_longitud - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ANCHO - TAM_CUADRADO) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTO - TAM_CUADRADO) / 20.0) * 20.0
            snake_longitud += 1

        reloj.tick(FPS)

    pygame.quit()
    sys.exit()

# Ejecutar juego
juego()
