import sys

import pygame

class AlienInvasion:
    """"Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """"Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")