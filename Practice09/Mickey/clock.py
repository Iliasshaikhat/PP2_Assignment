import pygame, datetime

pygame.init()

screen = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()

clockpng = pygame.image.load("images/clock.PNG")
leftpng = pygame.image.load("images/lefthand.PNG")
rightpng = pygame.image.load("images/righthand.PNG")

center = (1280 // 2, 960 // 2)

running = True

while running:
    now = datetime.datetime.now()
    

    minutes = now.minute
    seconds = now.second


    min_ang = minutes * 6 + seconds * 0.1
    sec_ang = seconds * 6

    min_rot = pygame.transform.rotate(rightpng, -min_ang)
    sec_rot = pygame.transform.rotate(leftpng, -sec_ang)

    min_rect = min_rot.get_rect(center=center)
    sec_rect = sec_rot.get_rect(center=center)

    screen.blit(clockpng, (0, 0))
    screen.blit(min_rot, min_rect)
    screen.blit(sec_rot, sec_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(144)  

pygame.quit()