#This code was created following Clear Code tutorials on the topic. 
#Este código foi criado seguindo os tutoriais do canal Clear Code.


import pygame, sys, random, time

#Animação da bola
#Ball's animation

def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x * deltaTime * fps_trav
    ball.y += ball_speed_y * deltaTime * fps_trav


    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1



#Animação do jogador
#Player's animation

def player_animation():
    player.y += player_speed * deltaTime * fps_trav
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

#IA do oponente
#Opponent's AI

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed * deltaTime * fps_trav

    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed * deltaTime * fps_trav

    if opponent.top <= 0:
        opponent.top = 0 
    
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


#Reseta a bola após colisão
#Resets ball's position after collision

def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))



#Setup

pygame.init()
clock = pygame.time.Clock()
tempo_init = time.time()

#Configuração da janela
#Window setup

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption('Pong')

#Formas geométricas do jogo
#Geometric forms

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 30, screen_height/2 - 70, 20, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 20, 140)

colorSurface = (63, 63, 90)
colorDefault = (255, 255, 255)

fps_trav = 60
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0

opponent_speed = 9

#Loop principal
while True:



    clock.tick(30)
    atual = time.time()
    deltaTime = atual - tempo_init
    tempo_init = atual

    #Detecção de input
    #Input detection
    for event in pygame.event.get():
        if event.type == None:
            player_speed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7 * deltaTime * fps_trav

            if event.key == pygame.K_UP:
                player_speed -= 7 * deltaTime * fps_trav

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7 * deltaTime * fps_trav
                
            if event.key == pygame.K_UP:
                player_speed += 7 * deltaTime * fps_trav


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    print(player_speed)
    
    ball_animation()
    player_animation()
    opponent_ai()

    #Visual
    screen.fill(colorSurface)

    pygame.draw.rect(screen, colorDefault, player)
    pygame.draw.rect(screen, colorDefault, opponent)
    pygame.draw.ellipse(screen, colorDefault, ball)
    pygame.draw.aaline(screen, colorDefault, (screen_width/2, 0), (screen_width/2, screen_height))


    #Atualização de frames
    pygame.display.flip()
