import pygame

pygame.init()

# -----------------------------
# HELPER
# -----------------------------
def draw_rounded_rect(surface, rect, color, radius=15):
    pygame.draw.rect(surface, color, rect, border_radius=radius)


# -----------------------------
# BUTTON
# -----------------------------
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

        self.base_color = (40, 40, 60)
        self.hover_color = (70, 70, 120)
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont("arial", 28)

        self.scale = 1.0  # animation

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        hovering = self.rect.collidepoint(mouse_pos)

        # animation (scale)
        if hovering:
            self.scale = min(1.05, self.scale + 0.02)
        else:
            self.scale = max(1.0, self.scale - 0.02)

        scaled_rect = self.rect.inflate(
            self.rect.width * (self.scale - 1),
            self.rect.height * (self.scale - 1)
        )

        # shadow
        shadow_rect = scaled_rect.move(4, 4)
        draw_rounded_rect(surface, shadow_rect, (0, 0, 0), 15)

        # button
        color = self.hover_color if hovering else self.base_color
        draw_rounded_rect(surface, scaled_rect, color, 15)

        # text
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=scaled_rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False


# -----------------------------
# TEXT INPUT
# -----------------------------
class TextInput:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.active = False

        self.font = pygame.font.SysFont("arial", 30)

        self.base_color = (30, 30, 50)
        self.active_color = (60, 60, 100)

        self.cursor_visible = True
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return self.text
            elif event.unicode.isprintable() and len(self.text) < 15:
                self.text += event.unicode

    def update(self):
        # blinking cursor
        self.cursor_timer += 1
        if self.cursor_timer > 30:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

    def draw(self, surface):
        color = self.active_color if self.active else self.base_color

        # shadow
        shadow = self.rect.move(3, 3)
        draw_rounded_rect(surface, shadow, (0, 0, 0), 12)

        # box
        draw_rounded_rect(surface, self.rect, color, 12)

        # text
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))

        # cursor
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 10 + text_surf.get_width() + 2
            pygame.draw.line(surface, (255, 255, 255),
                             (cursor_x, self.rect.y + 10),
                             (cursor_x, self.rect.y + 35), 2)