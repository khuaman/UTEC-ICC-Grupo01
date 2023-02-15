import sys
import pygame
#Inicializar
pygame.init()
#Colores
blanco = (255,255,255)
negro = (0,0,0)
gris = (122,122,122)
#Ancho y Alto de la Pantalla
pantalla_x = 1092
pantalla_y = 614
tamaño_pantalla = (pantalla_x,pantalla_y)
#Tamaño estándar de las paletas
ancho_jugador = 10
alto_jugador = 80
#Generar la pantalla
pantalla = pygame.display.set_mode(tamaño_pantalla)
pygame.display.set_caption('PROYECTO PONG GAME - ICC DREAM TEAM')
basic_font = pygame.font.Font('freesansbold.ttf', 32)
#Reloj: FPS
reloj = pygame.time.Clock()
#Coordenadas del jugador 1
jugador1_x = 10
jugador1_y = 267
#Coordenadas del jugador 2
jugador2_x = 1072
jugador2_y = 267
#Movimiento de los jugadores
mov_jugador1 = 0
mov_jugador2 = 0
#Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
mov_pelota_x = 3
mov_pelota_y = 3
#Flag: bandera de fin del juego
game_over = False
#Velocidad del juego
ticks = 60
#------------------------------
# Puntuación
# ------------------------------
    #establecer puntos
puntaje1 = 0
puntaje2 = 0
general = 0
if puntaje2 == 10 or puntaje1 == 10:
    game_over = True
while not game_over:
    # Gestión de Eventos: capturar eventos del Mouse y Teclado
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:
            game_over = True
        #Si se presiona una tecla, evaluar
        if evento.type == pygame.KEYDOWN:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = -3 #ir hacia arriba
            if evento.key == pygame.K_s:
                mov_jugador1 = 3 #ir hacia abajo
            #Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = -3 #ir hacia arriba
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 3 #ir hacia abajo
        #Si se deja de presiona la tecla, hay que detener la paleta
        if evento.type == pygame.KEYUP:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = 0 #ir hacia arriba
            if evento.key == pygame.K_s:
                mov_jugador1 = 0 #ir hacia abajo
            #Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = 0 #ir hacia arriba
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 0 #ir hacia abajo

    #Validación de la pelota: efecto rebote
    if pelota_y > pantalla_y-10 or pelota_y < 10:
        mov_pelota_y *=-1
    #Si la pelota sale por el lado izquierdo, o derecho, es porque alguien perdió
    if pelota_x > pantalla_x or pelota_x < 0:
        pelota_x = 546
        pelota_y = 307
        #Si sale de la pantalla, invertimos la dirección
        mov_pelota_x *= -1
        mov_pelota_y *= -1
    #Mover a los jugadores
    jugador1_y += mov_jugador1
    jugador2_y += mov_jugador2
    #Mover la pelota
    pelota_x +=mov_pelota_x
    pelota_y +=mov_pelota_y

    if pelota_x > pantalla_x:
        puntaje1 +=1
        general += 1
    if pelota_x < 0:
        puntaje2 +=1
        general +=1
        
    #Rebote de los rectángulos
    if jugador1_y+80 > pantalla_y or jugador1_y < 0:
        mov_jugador1 *= -1
    if jugador2_y+80 > pantalla_y or jugador2_y < 0:
        mov_jugador2 *= -1
    #------------------------------
    # Dibujos
    # ------------------------------
    #Dibujamos el fondo
    pantalla.fill(negro)
    #Dibujamos el jugador 1
    jugador1 = pygame.draw.rect(pantalla, blanco, (jugador1_x, jugador1_y, ancho_jugador, alto_jugador))
    #Dibujamos el jugador 2
    jugador2 = pygame.draw.rect(pantalla, blanco, (jugador2_x, jugador2_y, ancho_jugador, alto_jugador))
    #Dibujamos la pelota
    pelota = pygame.draw.circle(pantalla, blanco, (pelota_x, pelota_y), 10)
    #Dibujamos una línea en el centro para que se vea bonito
    pygame.draw.line(pantalla, gris , [pantalla_x//2,0] , [pantalla_x//2,pantalla_y] , 5)
    #SCORE
    #imprimir en pantalla la puntuación

    jugador1_text = basic_font.render(f'{puntaje1}', False, blanco)
    pantalla.blit(jugador1_text, (273, 100))

    jugador2_text = basic_font.render(f'{puntaje2}', False, blanco)
    pantalla.blit(jugador2_text, (819, 100))

    #Detección de colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        mov_pelota_x*=-1
    pygame.display.flip()

    reloj.tick(ticks)

    if general%2==0 and general > 0:
        ticks += 0.25 
    
    #Finalizar juego
    if puntaje1 == 10 or puntaje2 == 10:
        game_over = True
    
pygame.quit()