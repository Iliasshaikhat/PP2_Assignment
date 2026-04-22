import pygame
pygame.init()

Width = 1000
Height = 800

screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

color = Black

keys = {
    pygame.K_0: White,
    pygame.K_1: Black,
    pygame.K_2: Red,
    pygame.K_3: Green,
    pygame.K_4: Blue,
}

mode = "draw"
start_pos = None
drawing = False
last_pos = None

canvas = pygame.Surface((Width, Height))
canvas.fill(White)


preview = pygame.Surface((Width, Height), pygame.SRCALPHA)

running = True

while running:


    preview.fill((0, 0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                color = keys[event.key]

            if event.key == pygame.K_d:
                mode = "draw"

            if event.key == pygame.K_e:
                mode = "eraser"

            if event.key == pygame.K_r:
                mode = "rect"

            if event.key == pygame.K_o:
                mode = "circle"

            if event.key == pygame.K_c:
                canvas.fill(White)

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
            last_pos = start_pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            # RECT
            if mode == "rect" and start_pos:
                end_pos = pygame.mouse.get_pos()

                rect = pygame.Rect(
                    min(start_pos[0], end_pos[0]),
                    min(start_pos[1], end_pos[1]),
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )

                pygame.draw.rect(canvas, color, rect, 2)

            # CIRCLE
            if mode == "circle" and start_pos:
                end_pos = pygame.mouse.get_pos()

                rect = pygame.Rect(
                    min(start_pos[0], end_pos[0]),
                    min(start_pos[1], end_pos[1]),
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )

                pygame.draw.ellipse(canvas, color, rect, 2)

            start_pos = None
            last_pos = None

    x, y = pygame.mouse.get_pos()

    # DRAW
    if drawing and mode in ["draw", "eraser"]:
        draw_color = White if mode == "eraser" else color

        if last_pos:
            pygame.draw.line(canvas, draw_color, last_pos, (x, y), 10)

        last_pos = (x, y)

    # PREVIEW RECT
    if drawing and mode == "rect" and start_pos:
        rect = pygame.Rect(
            min(start_pos[0], x),
            min(start_pos[1], y),
            abs(x - start_pos[0]),
            abs(y - start_pos[1])
        )

        pygame.draw.rect(preview, color, rect, 2)

    # PREVIEW CIRCLE
    if drawing and mode == "circle" and start_pos:
        rect = pygame.Rect(
            min(start_pos[0], x),
            min(start_pos[1], y),
            abs(x - start_pos[0]),
            abs(y - start_pos[1])
        )

        pygame.draw.ellipse(preview, color, rect, 2)

    
    screen.blit(canvas, (0, 0))
    screen.blit(preview, (0, 0))

    pygame.display.flip()
    clock.tick(144)