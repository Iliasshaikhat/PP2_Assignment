import pygame
import sys
import os
from persistence import load_settings, save_settings, load_leaderboard, save_score
from ui import Button, TextInput
from racer import Player, Enemy, Obstacle, PowerUp

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

settings = load_settings()

road_img = pygame.image.load(os.path.join('assets', 'images', 'AnimatedStreet.png')).convert()
road_img = pygame.transform.scale(road_img, (300, 600))
road_y = 0


def load_sound(name):
    path = os.path.join('assets', 'sounds', name)
    try:
        return pygame.mixer.Sound(path)
    except (FileNotFoundError, pygame.error) as e:
        print(f"Warning: Could not load {name}. Error: {e}")
        return None

snd_crash = load_sound('crash.wav')
snd_powerup = load_sound('powerup.wav')

music_loaded = False
try:
    pygame.mixer.music.load(os.path.join('assets', 'sounds'))
    music_loaded = True
except:
    print("Warning: bg_music.mp3 not found.")

state = "MENU"
player_name = "Player"
score = 0
distance = 0
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
powerups = pygame.sprite.Group()
player = None

def reset_game():
    global player, score, distance, all_sprites, enemies, obstacles, powerups, road_y
    all_sprites.empty()
    enemies.empty()
    obstacles.empty()
    powerups.empty()
    player = Player(settings["car_color"])
    all_sprites.add(player)
    score = 0
    distance = 0
    road_y = 0

    if music_loaded and settings["sound"]:
        pygame.mixer.music.play(-1)

def draw_hud():
    screen.blit(font.render(f"Score: {int(score)}", True, (255,255,255)), (10, 10))
    screen.blit(font.render(f"Dist: {int(distance)}m", True, (255,255,255)), (10, 40))

    if player and player.nitro_active:
        time_left = (player.powerup_timer - pygame.time.get_ticks()) // 1000
        screen.blit(font.render(f"NITRO: {max(0, time_left)}s", True, (0, 255, 255)), (10, 80))

    if player and player.shield_active:
        screen.blit(font.render("SHIELD ACTIVE", True, (255, 215, 0)), (10, 80))
    

btn_play = Button(200, 150, 200, 50, "Play")
btn_board = Button(200, 220, 200, 50, "Leaderboard")
btn_settings = Button(200, 290, 200, 50, "Settings")
btn_quit = Button(200, 360, 200, 50, "Quit")

btn_easy = Button(200, 150, 200, 50, "Easy")
btn_normal = Button(200, 220, 200, 50, "Normal")
btn_hard = Button(200, 290, 200, 50, "Hard")

btn_back = Button(200, 500, 200, 50, "Back")
btn_retry = Button(200, 350, 200, 50, "Retry")
btn_menu = Button(200, 420, 200, 50, "Main Menu")

name_input = TextInput(200, 250, 200, 40)

SPAWN_ENEMY = pygame.USEREVENT + 1
SPAWN_OBSTACLE = pygame.USEREVENT + 2
SPAWN_POWERUP = pygame.USEREVENT + 3

pygame.time.set_timer(SPAWN_ENEMY, 1500)
pygame.time.set_timer(SPAWN_OBSTACLE, 2500)
pygame.time.set_timer(SPAWN_POWERUP, 6000)

running = True
while running:
    screen.fill((50, 150, 50))
    speed_boost = score // 500
    road_y += int(5 + speed_boost)

    if road_y >= HEIGHT:
        road_y = 0

    screen.blit(road_img, (150, road_y - HEIGHT))
    screen.blit(road_img, (150, road_y))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if state == "MENU":
            if btn_play.is_clicked(event): state = "NAME_INPUT"
            if btn_board.is_clicked(event): state = "LEADERBOARD"
            if btn_settings.is_clicked(event): state = "SETTINGS"
            if btn_quit.is_clicked(event): running = False

        elif state == "SETTINGS":
            if btn_back.is_clicked(event): state = "MENU"
            if btn_easy.is_clicked(event):
                settings["difficulty"] = "easy"
                save_settings(settings)
            if btn_normal.is_clicked(event):
                settings["difficulty"] = "normal"
                save_settings(settings)
            if btn_hard.is_clicked(event):
                settings["difficulty"] = "hard"
                save_settings(settings)

        elif state == "NAME_INPUT":
            name_input.handle_event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player_name = name_input.text if name_input.text else "Player"
                reset_game()
                state = "PLAY"

        elif state == "PLAY":
            speed_boost = score // 500

            if event.type == SPAWN_ENEMY:
                e = Enemy(settings["difficulty"])
                e.speed += speed_boost
                if not pygame.sprite.spritecollideany(e, enemies) and not pygame.sprite.spritecollideany(e, obstacles):
                    all_sprites.add(e)
                    enemies.add(e)

            if event.type == SPAWN_OBSTACLE:
                o = Obstacle()
                if not pygame.sprite.spritecollideany(o, enemies) and not pygame.sprite.spritecollideany(o, obstacles):
                    all_sprites.add(o)
                    obstacles.add(o)

            if event.type == SPAWN_POWERUP:
                p = PowerUp()
                if not pygame.sprite.spritecollideany(p, enemies) and not pygame.sprite.spritecollideany(p, obstacles):
                    all_sprites.add(p)
                    powerups.add(p)

        elif state == "LEADERBOARD":
            if btn_back.is_clicked(event): state = "MENU"

        elif state == "GAMEOVER":
            if btn_retry.is_clicked(event):
                reset_game()
                state = "PLAY"
            if btn_menu.is_clicked(event): state = "MENU"

    if state == "MENU":
        btn_play.draw(screen)
        btn_board.draw(screen)
        btn_settings.draw(screen)
        btn_quit.draw(screen)

    elif state == "SETTINGS":
        screen.fill((40, 40, 40))
        title = font.render("Difficulty Settings", True, (255, 255, 255))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        curr_diff = font.render(f"Current: {settings['difficulty'].upper()}", True, (0, 255, 0))
        screen.blit(curr_diff, (WIDTH//2 - curr_diff.get_width()//2, 380))

        btn_easy.draw(screen)
        btn_normal.draw(screen)
        btn_hard.draw(screen)
        btn_back.draw(screen)

    elif state == "NAME_INPUT":
        screen.blit(font.render("Enter Name & Press Enter:", True, (255,255,255)), (150, 200))
        name_input.draw(screen)

    elif state == "PLAY":
        all_sprites.update()

        speed_boost = score // 500
        distance += (0.1 + (speed_boost * 0.02))
        score += 0.2 if not player.nitro_active else 0.8

        if not player.shield_active:
            if pygame.sprite.spritecollideany(player, enemies) or pygame.sprite.spritecollideany(player, obstacles):
                if settings["sound"] and snd_crash: snd_crash.play()
                if player.crashes_allowed > 0:
                    player.crashes_allowed -= 1
                    player.shield_active = True
                    player.powerup_timer = pygame.time.get_ticks() + 2000
                else:
                    pygame.mixer.music.stop()
                    save_score(player_name, int(score), int(distance))
                    state = "GAMEOVER"

        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if settings["sound"] and snd_powerup: snd_powerup.play()

            if hit.type == "Nitro":
                player.nitro_active, player.shield_active = True, False
                player.powerup_timer = pygame.time.get_ticks() + 4000

            elif hit.type == "Shield":
                player.shield_active, player.nitro_active = True, False
                player.powerup_timer = pygame.time.get_ticks() + 4000

            elif hit.type == "Repair":
                player.crashes_allowed = 1

        all_sprites.draw(screen)
        draw_hud()

    elif state == "LEADERBOARD":
        screen.fill((30, 30, 30))
        board = load_leaderboard()
        for i, entry in enumerate(board):
            txt = f"{i+1}. {entry['name']} - {entry['score']} pts"
            screen.blit(font.render(txt, True, (255,255,255)), (150, 50 + i*35))
        btn_back.draw(screen)

    elif state == "GAMEOVER":
        screen.fill((0, 0, 0))
        screen.blit(font.render(f"GAME OVER! Score: {int(score)}", True, (255, 0, 0)), (180, 200))
        btn_retry.draw(screen)
        btn_menu.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()