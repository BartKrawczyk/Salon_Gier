Kod gry zotał wygenerowany przez Chat GPT.
Grafika początkowa została wygenerowana za pomocą AI Greem.

Dokumentacja gry "Wąż"
Opis

Ten kod reprezentuje grę "Wąż", stworzoną przy użyciu biblioteki Pygame. Gracz steruje wężem, który porusza się po ekranie. Celem gry jest zjadanie jabłek, które pojawiają się w różnych miejscach na ekranie. Każde zjedzone jabłko zwiększa długość węża oraz punktację gracza. Gra kończy się, gdy wąż uderzy w siebie.
Instrukcja obsługi
Uruchamianie gry

    Zainstaluj bibliotekę Pygame, jeśli nie jest jeszcze zainstalowana. Można to zrobić za pomocą polecenia pip install pygame.
    Uruchom grę, wykonując skrypt Pythona.

Sterowanie

    Użyj klawiszy strzałek na klawiaturze, aby poruszać wężem.
    Klawisz strzałki w górę porusza wężem do góry.
    Klawisz strzałki w dół porusza wężem w dół.
    Klawisz strzałki w lewo porusza wężem w lewo.
    Klawisz strzałki w prawo porusza wężem w prawo.

Zasady gry

    Wąż zaczyna grę z jednym segmentem i porusza się po ekranie.
    Pojawia się jabłko w losowym miejscu na ekranie.
    Gdy wąż zje jabłko, jego długość wzrasta o jeden segment i na ekranie pojawia się kolejne jabłko.
    Każde zjedzone jabłko zwiększa punktację gracza o 1 punkt.
    Gdy wąż zderzy się ze sobą, gra kończy się i gracz przenoszony jest do ekranu końcowego, gdzie wyświetlany jest jego wynik.
    Gracz ma możliwość rozpoczęcia nowej gry po naciśnięciu klawisza 'Enter', lub zakończenia gry poprzez naciśnięcie 'Q'.

Funkcje
reset_apple()

Ta funkcja generuje nowe jabłko w losowym miejscu na ekranie.
show_end_screen(score)

Ta funkcja wyświetla ekran końcowy po zakończeniu gry. Wyświetla wynik gracza i czeka 3 sekundy przed zakończeniem ekranu końcowego.
game_menu()

Ta funkcja wyświetla menu gry. Gracz może rozpocząć nową grę naciskając 'Enter', lub wyjść z gry naciskając 'Q'.
game_over()

Ta funkcja jest wywoływana, gdy wąż zderzy się z samym sobą. Wywołuje funkcję show_end_screen(score) i przenosi gracza do menu gry.
Zmienne
WIDTH, HEIGHT

Szerokość i wysokość okna gry.
BLOCK_SIZE

Rozmiar jednego segmentu węża i jabłka.
snake

Lista reprezentująca segmenty węża.
direction

Kierunek, w którym porusza się wąż.
apple

Pozycja jabłka na ekranie.
game_state

Stan gry, może przyjmować wartości "MENU", "PLAYING", "GAME_OVER".
score

Punktacja gracza.
speed

Prędkość, z jaką porusza się wąż. Wraz z wzrostem punktacji gracza, prędkość ta wzrasta.
Uwagi końcowe

Gracz powinien unikać zderzenia węża z samym sobą. Prędkość gry wzrasta wraz z postępem gracza, co zwiększa poziom trudności. Wysoki wynik wymaga precyzyjnego sterowania i szybkich decyzji.
