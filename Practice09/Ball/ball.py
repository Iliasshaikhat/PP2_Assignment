import pygame
pygame.init()

Width = 1200
Height = 800

screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

Red = (255, 0, 0)
White = (255, 255, 255)

x = Width // 2
y = Height // 2
r = 25
speed = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if y - speed - r >= 0:
            y -= speed

    if keys[pygame.K_DOWN]:
        if y + speed + r <= Height:
            y += speed

    if keys[pygame.K_LEFT]:
        if x - speed - r >= 0:
            x -= speed

    if keys[pygame.K_RIGHT]:
        if x + speed + r <= Width:
            x += speed

    screen.fill(White)

    pygame.draw.circle(screen, Red, (int(x), int(y)), r)

    pygame.display.flip()
    clock.tick(144)

pygame.quit()