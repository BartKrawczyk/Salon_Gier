import os
import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Menu Gry")

# Kolor tła
background_color = (255, 255, 255)

# Kolor przycisków
button_color = (215, 215, 215)
button_hover_color = (150, 150, 150)

# Font
font = pygame.font.Font(None, 36)

# Przyciski w menu
buttons = [
    {
        "text": "Galaga",
        "filename": "Galaga.py",
        "rect": pygame.Rect(window_width // 2 - 100, 200, 200, 50),
        "color": button_color,
        "hover": False
    },
    {
        "text": "Snake",
        "filename": "snake.py",
        "rect": pygame.Rect(window_width // 2 - 100, 300, 200, 50),
        "color": button_color,
        "hover": False
    },
    {
        "text": "Zakończ",
        "rect": pygame.Rect(window_width // 2 - 100, 400, 200, 50),
        "color": button_color,
        "hover": False
    }
]

# Grafika tła
background_image = pygame.image.load("background-menu.png")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Główna pętla menu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Kliknięcie lewym przyciskiem myszy
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button["rect"].collidepoint(pos):
                    if "filename" in button:
                        # Uruchomienie gry w osobnym oknie
                        os.startfile(button["filename"])
                    else:
                        # Zamknięcie okna menu
                        running = False

    # Rysowanie tła
    window.blit(background_image, (0, 0))

    # Rysowanie przycisków
    for button in buttons:
        if button["hover"]:
            pygame.draw.rect(window, button_hover_color, button["rect"])
        else:
            pygame.draw.rect(window, button["color"], button["rect"])

        # Rysowanie tekstu w przyciskach
        text_surface = font.render(button["text"], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button["rect"].center)
        window.blit(text_surface, text_rect)

    # Aktualizacja stanu przycisków
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button["rect"].collidepoint(pos):
            button["hover"] = True
        else:
            button["hover"] = False

    # Aktualizacja wyświetlanego ekranu
    pygame.display.flip()

# Zakończenie programu
pygame.quit()
