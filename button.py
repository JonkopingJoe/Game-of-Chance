import pygame
class Button(pygame.sprite.Sprite):
    def __init__(
        self, text: str, text_color: tuple, bg_color: tuple, width: int, height: int
    ):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(bg_color)
        self.rect = self.image.get_rect()

        # default font
        button_font = pygame.font.SysFont("monospace", 20)

        # Render text and align
        self.render_text = button_font.render(text, True, text_color, bg_color)
        self.text_rect = self.render_text.get_rect()

        self.image.blit(self.render_text, self.text_rect)

    def is_clicked(self, event) -> bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.text_rect.collidepoint(event.pos)
        )

