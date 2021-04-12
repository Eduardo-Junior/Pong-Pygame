import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y


    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed

    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0 
    
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
#Setup

pygame.init()
clock = pygame.time.Clock()

#Configuração da janela

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pong')

#Formas geométricas do jogo

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 30, screen_height/2 - 70, 20, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 20, 140)

colorSurface = (63, 63, 90)
colorDefault = (255, 255, 255)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0

playerAI_speed, opponent_speed = 7, 7

#Loop principal
while True:

    #Recebendo input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
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
    clock.tick(60)