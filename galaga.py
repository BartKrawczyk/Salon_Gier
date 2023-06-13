import pygame
import sys
import random

# Konfiguracja
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 30, 30
LASER_WIDTH, LASER_HEIGHT = 10, 20
FPS = 60

# Kolor
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Inicjalizacja Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Grafiki
background_image = pygame.image.load('background_galaga.png').convert()
player_image = pygame.image.load('player.png').convert_alpha()
enemy_image = pygame.image.load('enemy.png').convert_alpha()
laser_image = pygame.image.load('laser.png').convert_alpha()

# Pozycja gracza
player_pos = pygame.Vector2(WIDTH / 2 - PLAYER_WIDTH / 2, HEIGHT - PLAYER_HEIGHT)

# Prędkość ruchu gracza
player_speed = pygame.Vector2(0, -5)

# Lista wrogów
enemies = []

# Lista laserów
lasers = []

# Licznik punktów
score = 0

# Stan gry
GameState = {"START_SCREEN": 0, "PLAYING": 1, "GAME_OVER": 2}
game_state = GameState["START_SCREEN"]

# Funkcja do tworzenia wrogów
def create_enemy():
    x = random.randint(0, WIDTH - ENEMY_WIDTH)
    y = random.randint(-HEIGHT, -ENEMY_HEIGHT)
    enemy_pos = pygame.Vector2(x, y)
    enemies.append(enemy_pos)

# Funkcja do tworzenia laserów
def create_laser():
    x = player_pos.x + PLAYER_WIDTH / 2 - LASER_WIDTH / 2
    y = player_pos.y
    laser_pos = pygame.Vector2(x, y)
    lasers.append(laser_pos)

# Funkcja wyświetlająca ekran startowy
def show_start_screen():
    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press ENTER to start or Q to quit", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Funkcja wyświetlająca ekran końcowy
def show_game_over_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game Over. Your score: {score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

# Główna pętla gry
running = True
while running:
    if game_state == GameState["START_SCREEN"]:
        show_start_screen()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = GameState["PLAYING"]
                elif event.key == pygame.K_q:
                    running = False

    elif game_state == GameState["PLAYING"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Strzelanie
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    create_laser()

        # Poruszanie się gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos.x -= 5
        if keys[pygame.K_RIGHT]:
            player_pos.x += 5

        # Aktualizacja pozycji wrogów
        for enemy_pos in enemies:
            enemy_pos.y += 3

            # Kolizja gracza z wrogiem
            if pygame.Rect(player_pos, (PLAYER_WIDTH, PLAYER_HEIGHT)).colliderect(
                    pygame.Rect(enemy_pos, (ENEMY_WIDTH, ENEMY_HEIGHT))):
                game_state = GameState["GAME_OVER"]

            # Usunięcie wroga z listy, gdy przekroczy dolną krawędź ekranu
            if enemy_pos.y > HEIGHT:
                enemies.remove(enemy_pos)

        # Aktualizacja pozycji laserów
        for laser_pos in lasers:
            laser_pos.y -= 5

            # Sprawdzenie kolizji lasera z wrogiem
            for enemy_pos in enemies:
                if pygame.Rect(laser_pos, (LASER_WIDTH, LASER_HEIGHT)).colliderect(
                        pygame.Rect(enemy_pos, (ENEMY_WIDTH, ENEMY_HEIGHT))):
                    lasers.remove(laser_pos)
                    enemies.remove(enemy_pos)
                    score += 1
                    break

            # Usunięcie lasera z listy, gdy przekroczy górną krawędź ekranu
            if laser_pos.y < 0:
                lasers.remove(laser_pos)

        # Tworzenie nowych wrogów
        if len(enemies) < 10:
            create_enemy()

        # Rysowanie
        screen.fill(BLACK)
        screen.blit(player_image, player_pos)
        for enemy_pos in enemies:
            screen.blit(enemy_image, enemy_pos)
        for laser_pos in lasers:
            screen.blit(laser_image, laser_pos)

        # Wyświetlanie punktacji
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    elif game_state == GameState["GAME_OVER"]:
        show_game_over_screen()
        game_state = GameState["START_SCREEN"]

pygame.quit()
