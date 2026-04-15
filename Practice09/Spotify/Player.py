import pygame
import os

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)


music_folder = r"C:\Python\Practice09\Spotify\Music"
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3") or f.endswith(".wav")]

current = 0
playing = False

def load_track(index):
    pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
    pygame.mixer.music.play()

def stop_track():
    pygame.mixer.music.stop()

running = True
while running:
    screen.fill((30, 30, 30))

    
    track_text = font.render(f"Track: {playlist[current]}", True, (255, 255, 255))
    screen.blit(track_text, (20, 20))

    status = "Playing" if playing else "Stopped"
    status_text = font.render(f"Status: {status}", True, (200, 200, 200))
    screen.blit(status_text, (20, 60))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            
            if event.key == pygame.K_p:
                load_track(current)
                playing = True

            
            if event.key == pygame.K_s:
                stop_track()
                playing = False

            
            if event.key == pygame.K_n:
                current = (current + 1) % len(playlist)
                load_track(current)
                playing = True

            
            if event.key == pygame.K_b:
                current = (current - 1) % len(playlist)
                load_track(current)
                playing = True

            
            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()