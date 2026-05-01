import pygame

def draw_rect(surface, color, start_pos, end_pos, width):
    rect = pygame.Rect(
        min(start_pos[0], end_pos[0]),
        min(start_pos[1], end_pos[1]),
        abs(end_pos[0] - start_pos[0]),
        abs(end_pos[1] - start_pos[1])
    )
    pygame.draw.rect(surface, color, rect, width)


def draw_circle(surface, color, start_pos, end_pos, width):
    rect = pygame.Rect(
        min(start_pos[0], end_pos[0]),
        min(start_pos[1], end_pos[1]),
        abs(end_pos[0] - start_pos[0]),
        abs(end_pos[1] - start_pos[1])
    )
    pygame.draw.ellipse(surface, color, rect, width)


def draw_line(surface, color, start_pos, end_pos, width):
    pygame.draw.line(surface, color, start_pos, end_pos, width)


def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if surface.get_at((px, py)) == target_color:
            surface.set_at((px, py), new_color)

            if px > 0:
                stack.append((px - 1, py))
            if px < surface.get_width() - 1:
                stack.append((px + 1, py))
            if py > 0:
                stack.append((px, py - 1))
            if py < surface.get_height() - 1:
                stack.append((px, py + 1))