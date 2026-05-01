import pygame
import datetime
from tools import draw_rect, draw_circle, draw_line, flood_fill

pygame.init()

Width = 1000
Height = 800

screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

White = (255, 255, 255)
Black = (0, 0, 0)
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
brush_size = 2

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
            # brush size
            mods = pygame.key.get_mods()
            if mods & pygame.KMOD_CTRL:
                if event.key == pygame.K_1:
                    brush_size = 2
                elif event.key == pygame.K_2:
                    brush_size = 5
                elif event.key == pygame.K_3:
                    brush_size = 10
            else :
                if event.key in keys:
                     color = keys[event.key]

            # modes
            if event.key == pygame.K_d:
                mode = "draw"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_o:
                mode = "circle"
            if event.key == pygame.K_l:
                mode = "line"
            if event.key == pygame.K_f:
                mode = "fill"

            

            # clear
            if event.key == pygame.K_c:
                canvas.fill(White)

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "fill":
                x, y = event.pos
                flood_fill(canvas, x, y, color)
            else:
                drawing = True
                start_pos = event.pos
                last_pos = start_pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos

                if mode == "rect":
                    draw_rect(canvas, color, start_pos, end_pos, brush_size)

                if mode == "circle":
                    draw_circle(canvas, color, start_pos, end_pos, brush_size)

                if mode == "line":
                    draw_line(canvas, color, start_pos, end_pos, brush_size)

            drawing = False
            start_pos = None
            last_pos = None

    x, y = pygame.mouse.get_pos()

    # pencil / eraser
    if drawing and mode in ["draw", "eraser"]:
        draw_color = White if mode == "eraser" else color

        if last_pos:
            pygame.draw.line(canvas, draw_color, last_pos, (x, y), brush_size)

        last_pos = (x, y)

    # preview shapes
    if drawing and start_pos:
        if mode == "rect":
            draw_rect(preview, color, start_pos, (x, y), brush_size)

        if mode == "circle":
            draw_circle(preview, color, start_pos, (x, y), brush_size)

        if mode == "line":
            draw_line(preview, color, start_pos, (x, y), brush_size)

    screen.blit(canvas, (0, 0))
    screen.blit(preview, (0, 0))

    pygame.display.flip()
    clock.tick(144)

pygame.quit()