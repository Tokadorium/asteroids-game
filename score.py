import pygame

from ui import UI
from constants import *


class Score(UI):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.count = 0

    def draw(self, screen):
        screen.blit(self.text_surface, (0, 0))

    def update(self, dt):
        self.text_surface = self.font.render(f"Score: {self.count}", False, (255, 255, 255))

    def inc_score(self):
        self.count += 1