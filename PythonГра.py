import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SuperArkanoid")

дошка = pygame.image.load("images/paddle.png")
цеглинка = pygame.image.load("images/brick_1.png")
мячик = pygame.image.load("images/ball.png")

#Координати розміщення дошки та швидкість її переміщення
x = 320
y = 565
speed = 2

#Координати для цеглинки
x_1 = 0
y_1 = 5


background_sound = pygame.mixer.Sound("Soundtrack/S31-Night Prowler.ogg")
background_sound.play()

#Вихід із гри
running = True
while running:


    screen.fill((227, 225, 225))
    #Розміщення дошки на екрані
    позиція_дошки = screen.blit(дошка, (x, y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    #Рух дошки
    кнопки_для_переміщення = pygame.key.get_pressed()

    if кнопки_для_переміщення[pygame.K_LEFT]:
        x -= speed
    if кнопки_для_переміщення[pygame.K_RIGHT]:
        x += speed

    #Границі для дошки
    if x <= -1:
        x = 0

    if x <= -1:
        x = 0

    if x >= 800:
        x = 800
    if x >= 672:
        x = 672












