import pygame
import random

x_paddle = 320
y_paddle = 565
speed = 5

lines = 4
columns = 11

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("SuperArkanoid")
    return screen

def load_images():
    paddle = pygame.image.load("images/paddle.png")
    brick = pygame.image.load("images/brick_1.png")
    ball = pygame.image.load("images/ball.png")
    return paddle, brick, ball

def play_background_sound():
    background_sound = pygame.mixer.Sound("Soundtrack/S31-Night Prowler.ogg")
    background_sound.play()

def draw_paddle(screen, paddle, x_paddle, y_paddle):
    screen.blit(paddle, (x_paddle, y_paddle))

def draw_ball(screen, ball, x_ball, y_ball):
    screen.blit(ball, (x_ball, y_ball))

def moving_ball(x_ball, y_ball, ball_dx, ball_dy):
    x_ball += ball_dx
    y_ball += ball_dy
    return x_ball, y_ball

def draw_bricks(screen, bricks, brick, lines, columns):
    x_offset = 9
    y_offset = 9
    for line in range(lines):
        for column in range(columns):
            if bricks[line][column] == 1:
                x_brick = column * (brick.get_width() + x_offset)
                y_brick = line * (brick.get_height() + y_offset)
                screen.blit(brick, (x_brick, y_brick))

def main():
    x_ball = 400
    y_ball = 300
    screen = init_game()
    paddle, brick, ball = load_images()
    play_background_sound()

    x_paddle = 320
    y_paddle = 565
    speed = 5

    ball_dx = 2
    ball_dy = 2

    running = True

    bricks = [[1 for _ in range(columns)] for _ in range(lines)]  

    while running:
        screen.fill((227, 225, 225))

        draw_paddle(screen, paddle, x_paddle, y_paddle)
        draw_bricks(screen, bricks, brick, lines, columns)
        draw_ball(screen, ball, x_ball, y_ball)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        moving_paddle = pygame.key.get_pressed()

        if moving_paddle[pygame.K_LEFT]:
            x_paddle -= speed
        if moving_paddle[pygame.K_RIGHT]:
            x_paddle += speed

        if x_paddle <= -1:
            x_paddle = 0
        if x_paddle >= 800 - paddle.get_width():
            x_paddle = 800 - paddle.get_width()

        if x_ball <= 0:
            ball_dx = abs(ball_dx)
        elif x_ball >= 800 - ball.get_width():
            ball_dx = -abs(ball_dx)

        if y_ball <= 0:
            ball_dy = abs(ball_dy)
        elif y_ball >= 600 - ball.get_height():
            running = False  

        
        if y_ball + ball.get_height() >= y_paddle and x_ball + ball.get_width() >= x_paddle and x_ball <= x_paddle + paddle.get_width():
            ball_dy = -ball_dy

        
        brick_width = brick.get_width()
        brick_height = brick.get_height()
        for line in range(lines):
            for column in range(columns):
                if bricks[line][column] == 1:  
                    x_brick = column * (brick_width + 9)
                    y_brick = line * (brick_height + 9)
                    brick_rect = pygame.Rect(x_brick, y_brick, brick_width, brick_height)
                    if brick_rect.colliderect(ball.get_rect(left=x_ball, top=y_ball)):
                        ball_dy = -ball_dy
                        bricks[line][column] = 0
                        break  

        x_ball, y_ball = moving_ball(x_ball, y_ball, ball_dx, ball_dy)

    pygame.quit()

main()
