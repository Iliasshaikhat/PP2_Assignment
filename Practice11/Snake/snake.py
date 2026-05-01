import pygame
import random

pygame.init()

# ------------------ GAME SETTINGS ------------------
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ------------------ COLORS ------------------
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BLUE = (0, 150, 255)
BLACK = (0, 0, 0)

# ------------------ SNAKE ------------------
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# ------------------ SCORE ------------------
score = 0
level = 1
food_eaten = 0
speed = 10

# ------------------ FOOD SYSTEM ------------------
# разные типы еды (цвет, score, weight, lifetime)
food_types = [
    (RED, 1, 60, 300),     # обычная еда
    (GOLD, 3, 30, 200),    # редкая
    (BLUE, 5, 10, 120)     # очень редкая
]

food = None
food_timer = 0

# ------------------ FOOD GENERATION (WEIGHTED) ------------------
def generate_food():
    """Создаёт еду с учётом веса (probability)"""
    total_weight = sum(f[2] for f in food_types)
    r = random.randint(1, total_weight)

    current = 0
    for color, value, weight, lifetime in food_types:
        current += weight
        if r <= current:
            while True:
                x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
                y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE

                if (x, y) not in snake:
                    return {
                        "pos": (x, y),
                        "color": color,
                        "value": value,
                        "lifetime": lifetime,
                        "timer": lifetime
                    }

# первая еда
food = generate_food()

# ------------------ MAIN LOOP ------------------
running = True

while running:
    screen.fill(BLACK)

    # ------------------ EVENTS ------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)

            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)

            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)

            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # ------------------ MOVE SNAKE ------------------
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # collision with walls
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False

    # collision with self
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # ------------------ FOOD TIMER ------------------
    if food:
        food["timer"] -= 1

        # если еда исчезла
        if food["timer"] <= 0:
            food = generate_food()

    # ------------------ EATING FOOD ------------------
    if food and new_head == food["pos"]:
        score += food["value"]
        food_eaten += 1

        food = generate_food()

        # уровень растёт каждые 3 еды
        if food_eaten >= 3:
            level += 1
            food_eaten = 0
            speed += 2

    else:
        snake.pop()

    # ------------------ DRAW SNAKE ------------------
    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                         (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # ------------------ DRAW FOOD ------------------
    if food:
        pygame.draw.rect(screen, food["color"],
                         (food["pos"][0], food["pos"][1], CELL_SIZE, CELL_SIZE))

    # ------------------ UI ------------------
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    timer_text = font.render(f"Food timer: {food['timer']}", True, WHITE)
    screen.blit(timer_text, (10, 35))

    # ------------------ UPDATE ------------------
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()