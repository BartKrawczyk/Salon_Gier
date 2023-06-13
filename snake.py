import pygame
import sys
import random

# Konfiguracja
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20

# Kolor
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicjalizacja Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)  # Dodałem czcionkę do wyświetlania tekstu


# Wąż
snake = [(WIDTH / 2, HEIGHT / 2)]
direction = 'RIGHT'

# Jabłko
apple = None

# Stan gry
GameState = {"MENU": 0, "PLAYING": 1, "GAME_OVER": 2}
game_state = GameState["MENU"]

# Funkcje
def reset_apple():
    global apple
    apple = (
        random.randrange(0, WIDTH, BLOCK_SIZE),
        random.randrange(0, HEIGHT, BLOCK_SIZE)
    )

def show_end_screen(score):
    screen.fill((0, 0, 0))
    text = font.render(f"Koniec gry. Twój wynik to {score} punktów.", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def game_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Rozpoczyna nową grę po naciśnięciu 'Enter'
                    return GameState["PLAYING"]
                if event.key == pygame.K_q:  # Wyjdź z gry po naciśnięciu 'q'
                    pygame.quit()
                    sys.exit()

        screen.blit(background, (0, 0))
        text = font.render(f"Snake Game - Wciśnij Enter aby rozpocząć, Q aby wyjść", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

def game_over():
    show_end_screen(len(snake) - 1)
    pygame.time.wait(3000)  # Czeka 3 sekundy przed zakończeniem ekranu końcowego
    return GameState["MENU"]

# Gra
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

score = 0  # Inicjalizacja wyniku
speed = 15  # Inicjalizacja prędkości

while True:
    if game_state == GameState["MENU"]:
        game_state = game_menu()
        snake = [(WIDTH / 2, HEIGHT / 2)]
        direction = 'RIGHT'
        reset_apple()
        score = 0  # Zerowanie wyniku
        speed = 15  # Zerowanie prędkości
        screen.blit(background, (0, 0))  # Dodaję tło do ekranu początkowego
    elif game_state == GameState["PLAYING"]:
        clock = pygame.time.Clock()
        running = True

        while running:
            # Kontrolki
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

            # Aktualizacja pozycji węża
            head = snake[0]
            if direction == 'UP':
                snake.insert(0, (head[0], (head[1] - BLOCK_SIZE) % HEIGHT))
            elif direction == 'DOWN':
                snake.insert(0, (head[0], (head[1] + BLOCK_SIZE) % HEIGHT))
            elif direction == 'LEFT':
                snake.insert(0, ((head[0] - BLOCK_SIZE) % WIDTH, head[1]))
            else:
                snake.insert(0, ((head[0] + BLOCK_SIZE) % WIDTH, head[1]))

            # Sprawdzenie kolizji z jabłkiem
            if snake[0] == apple:
                reset_apple()
                score += 1  # Zwiększa wynik za każde zjedzone jabłko
                if score % 10 == 0:  # Zwiększ prędkość co 10 zdobytych punktów
                    speed += 1
            else:
                snake.pop()

            # Sprawdzenie kolizji z samym sobą
            if snake[0] in snake[1:]:
                running = False

            # Rysowanie
            screen.fill((0, 0, 0))
            for segment in snake:
                pygame.draw.rect(screen, WHITE, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, RED, pygame.Rect(apple[0], apple[1], BLOCK_SIZE, BLOCK_SIZE))

            # Wyświetlanie wyniku
            score_text = font.render(f"Wynik: {score}", True, WHITE)
            score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
            screen.blit(score_text, score_rect)

            pygame.display.flip()

            # Kontrola prędkości
            clock.tick(speed)

        game_state = GameState["GAME_OVER"]
    elif game_state == GameState["GAME_OVER"]:
        game_state = game_over()
        screen.blit(background, (0, 0))  # Dodaję tło do ekranu końcowego


