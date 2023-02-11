import pygame.font

class Scoreboard:
    """Клас для виведення ігрової інформації"""

    def __init__(self, ai_game):
        """Ініціалізує атрибути підрахунку очок"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифта для виведення очок
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Підготовка вихідного зображення
        self.prep_score()

    def prep_score(self):
        """Перетворює поточний рахунок на графічне зображення"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Виведення рахунку в правій верхній частині екрану
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_score(self):
        """Виводе рахунок на екран"""
        self.screen.blit(self.score_image, self.score_rect)
        