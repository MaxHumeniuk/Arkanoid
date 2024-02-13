import pygame
import random

x_paddle = 320
y_paddle = 565
speed = 5


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


def draw_bricks(screen, bricks, brick_width, brick_height, x_ball, y_ball, ball_width, ball_height, ball_dx, ball_dy):
    for brick in bricks:
        if brick is not None:  
            screen.blit(brick["image"], brick["rect"])
            if brick["rect"].colliderect(pygame.Rect(x_ball, y_ball, ball_width, ball_height)):
                bricks.remove(brick)
                return True  
    return False 



def main():
    x_ball = 400
    y_ball = 300
    screen = init_game()
    paddle, brick_img, ball = load_images()
    play_background_sound()

    x_paddle = 320
    y_paddle = 565
    speed = 5

    ball_dx = 2
    ball_dy = 2

    brick_width = brick_img.get_width()
    brick_height = brick_img.get_height()

    bricks = [{"image": brick_img, "rect": pygame.Rect((brick_width * i) + 10, (brick_height * j) + 10, brick_width, brick_height)} for i in range(12) for j in range(4)]

    score = 0  

    running = True

    while running:
        screen.fill("white")

        
        draw_paddle(screen, paddle, x_paddle, y_paddle)
        ball_hit_brick = draw_bricks(screen, bricks, brick_width, brick_height, x_ball, y_ball, ball.get_width(), ball.get_height(), ball_dx, ball_dy)
        if ball_hit_brick:
            ball_dy = -ball_dy
            score += 5

        draw_ball(screen, ball, x_ball, y_ball)

        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, "black")
        screen.blit(score_text, (10, 500))

        pygame.display.update()

        
        if score >= 240:
            win_text = font.render("You Win!!!!!!! ", True, "black")
            screen.blit(win_text, (400, 300))
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() 
        
        pygame.display.update()

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

        x_ball, y_ball = moving_ball(x_ball, y_ball, ball_dx, ball_dy)

    pygame.quit()

main()
