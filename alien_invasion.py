import sys

import pygame

class AlienInvasion:
    """"Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """"Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """"Запуск основного цикла игры."""

        while True:
            # Отслеживание клавиш и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерысовывает экран.
            self.screen.fill(self.bg_color)
            # Отображение последнего прорисованого экрана
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и создание игры
    ai = AlienInvasion()
    ai.run_game()