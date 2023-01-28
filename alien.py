import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас для одного прибульця"""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його почтакову позицію"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантаження зображення прибульця та призначення атрибуту rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється у лівому верхньому куті
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Збереження точної горизонтальної позиції прибульця
        self.x = float(self.rect.x)

    def update(self):
        """Переміщує прибульця праовруч"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
         