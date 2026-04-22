import pygame
import random
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1400, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game(ШАШКИ)")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(__file__)

def load_path(*path):
    return os.path.join(BASE_DIR, *path)

road = pygame.image.load(load_path("image", "road.png"))
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

car_img = pygame.image.load(load_path("image", "car.png"))
car_img = pygame.transform.scale(car_img, (80, 140))

enemy_img1 = pygame.image.load(load_path("image", "enemy.png"))
enemy_img1 = pygame.transform.scale(enemy_img1, (80, 140))

enemy_img2 = pygame.image.load(load_path("image", "enemy2.png"))
enemy_img2 = pygame.transform.scale(enemy_img2, (80, 140))

enemy_images = [enemy_img1, enemy_img2]

music_folder = load_path("music")

playlist = [
    os.path.join(music_folder, f)
    for f in os.listdir(music_folder)
    if f.endswith(".mp3") or f.endswith(".wav")
]

playlist.sort()



current_track = 0
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play(-1)

road_y = 0
base_speed = 10  

car = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 160, 80, 140)

coins = []
coin_timer = 0
score = 0

enemies = []
enemy_timer = 0

game_over = False

font = pygame.font.SysFont("Arial", 30)

running = True
while running:
    clock.tick(60)

    speed = base_speed + score * 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            
            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_p:
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_m:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            
            if game_over and event.key == pygame.K_r:
                game_over = False
                score = 0
                coins.clear()
                enemies.clear()
                car.x = WIDTH // 2 - 40

    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            car.x -= 10

        if keys[pygame.K_RIGHT]:
            car.x += 10

        if car.x < 0:
            car.x = 0
        if car.x > WIDTH - car.width:
            car.x = WIDTH - car.width

        road_y += speed
        if road_y >= HEIGHT:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - HEIGHT))

        coin_timer += 1
        if coin_timer > 40:
            x = random.randint(50, WIDTH - 50)
            coins.append(pygame.Rect(x, -20, 25, 25))
            coin_timer = 0

        for coin in coins[:]:
            coin.y += speed

            if car.colliderect(coin):
                coins.remove(coin)
                score += 1

            elif coin.y > HEIGHT:
                coins.remove(coin)

        enemy_timer += 1
        if enemy_timer > 50:
            x = random.randint(50, WIDTH - 130)
            rect = pygame.Rect(x, -150, 80, 140)
            img = random.choice(enemy_images)
            enemies.append([rect, img])
            enemy_timer = 0

        for enemy in enemies[:]:
            enemy[0].y += speed + 3

            if car.colliderect(enemy[0]):
                game_over = True

            if enemy[0].y > HEIGHT:
                enemies.remove(enemy)

        screen.blit(car_img, (car.x, car.y))

        for coin in coins:
            pygame.draw.circle(screen, (255, 215, 0), coin.center, 12)

        for enemy in enemies:
            screen.blit(enemy[1], (enemy[0].x, enemy[0].y))

        # UI
        screen.blit(font.render(f"Coins: {score}", True, (255, 255, 255)), (WIDTH - 170, 10))
        screen.blit(font.render(f"Speed: {int(speed)}", True, (200, 200, 200)), (10, 10))
        screen.blit(font.render(f"Track: {current_track + 1}", True, (200, 200, 200)), (10, 40))

    else:
        screen.fill((0, 0, 0))

        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (WIDTH//2 - 120, HEIGHT//2 - 50))
        screen.blit(font.render("Press R to restart", True, (255, 255, 255)), (WIDTH//2 - 150, HEIGHT//2 + 10))
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 0)), (WIDTH//2 - 80, HEIGHT//2 + 60))

    pygame.display.flip()

pygame.quit()