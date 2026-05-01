import pygame
pygame.init()

# ------------------ WINDOW ------------------
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ------------------ COLORS ------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = BLACK

# ------------------ KEY COLORS ------------------
keys = {
    pygame.K_0: WHITE,
    pygame.K_1: BLACK,
    pygame.K_2: RED,
    pygame.K_3: GREEN,
    pygame.K_4: BLUE,
}

# ------------------ MODES ------------------
mode = "draw"
drawing = False
start_pos = None
last_pos = None

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

preview = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# ------------------ MAIN LOOP ------------------
running = True

while running:
    clock.tick(144)

    preview.fill((0, 0, 0, 0))

    # ------------------ EVENTS ------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ------------------ KEYBOARD ------------------
        if event.type == pygame.KEYDOWN:

            if event.key in keys:
                color = keys[event.key]

            elif event.key == pygame.K_d:
                mode = "draw"

            elif event.key == pygame.K_e:
                mode = "eraser"

            elif event.key == pygame.K_r:
                mode = "rect"

            elif event.key == pygame.K_o:
                mode = "circle"

            elif event.key == pygame.K_s:
                mode = "square"

            elif event.key == pygame.K_t:
                mode = "triangle_right"

            elif event.key == pygame.K_y:
                mode = "triangle_equilateral"

            elif event.key == pygame.K_h:
                mode = "rhombus"

            elif event.key == pygame.K_c:
                canvas.fill(WHITE)

        # ------------------ MOUSE DOWN ------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
            last_pos = start_pos

        # ------------------ MOUSE UP (FINAL DRAW) ------------------
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if start_pos:
                x1, y1 = start_pos
                x2, y2 = pygame.mouse.get_pos()

                # ------------------ RECTANGLE ------------------
                if mode == "rect":
                    rect = pygame.Rect(
                        min(x1, x2),
                        min(y1, y2),
                        abs(x2 - x1),
                        abs(y2 - y1)
                    )
                    pygame.draw.rect(canvas, color, rect, 2)

                # ------------------ SQUARE ------------------
                elif mode == "square":
                    size = min(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, size, size)
                    pygame.draw.rect(canvas, color, rect, 2)

                # ------------------ RIGHT TRIANGLE ------------------
                elif mode == "triangle_right":
                    points = [(x1, y1), (x1, y2), (x2, y2)]
                    pygame.draw.polygon(canvas, color, points, 2)

                # ------------------ EQUILATERAL TRIANGLE ------------------
                elif mode == "triangle_equilateral":
                    height = int((3 ** 0.5 / 2) * abs(x2 - x1))

                    points = [
                        (x1, y2),
                        (x2, y2),
                        ((x1 + x2) // 2, y2 - height)
                    ]
                    pygame.draw.polygon(canvas, color, points, 2)

                # ------------------ RHOMBUS ------------------
                elif mode == "rhombus":
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    points = [
                        (cx, y1),
                        (x2, cy),
                        (cx, y2),
                        (x1, cy)
                    ]
                    pygame.draw.polygon(canvas, color, points, 2)

            start_pos = None
            last_pos = None

    # ------------------ FREE DRAW ------------------
    x, y = pygame.mouse.get_pos()

    if drawing and mode in ["draw", "eraser"]:
        draw_color = WHITE if mode == "eraser" else color

        if last_pos:
            pygame.draw.line(canvas, draw_color, last_pos, (x, y), 8)

        last_pos = (x, y)

    # ------------------ PREVIEW RECT ------------------
    if drawing and start_pos and mode == "rect":
        x1, y1 = start_pos
        rect = pygame.Rect(
            min(x1, x),
            min(y1, y),
            abs(x - x1),
            abs(y - y1)
        )
        pygame.draw.rect(preview, color, rect, 2)

    # ------------------ PREVIEW CIRCLE ------------------
    if drawing and start_pos and mode == "circle":
        x1, y1 = start_pos
        rect = pygame.Rect(
            min(x1, x),
            min(y1, y),
            abs(x - x1),
            abs(y - y1)
        )
        pygame.draw.ellipse(preview, color, rect, 2)

    # ------------------ DRAW TO SCREEN ------------------
    screen.blit(canvas, (0, 0))
    screen.blit(preview, (0, 0))

    pygame.display.flip()

pygame.quit()