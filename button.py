import pygame
class Button(pygame.sprite.Sprite):
    def __init__(
        self, text: str, text_color: tuple, bg_color: tuple, width: int, height: int
    ):
        super().__init__()

        # Default font
        button_font = pygame.font.Font(None, 36)

        # Render text and align
        self.render_text = button_font.render(text, True, text_color, bg_color)
        self.text_rect = self.render_text.get_rect()

    def is_clicked(self, event) -> bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.text_rect.collidepoint(event.pos)
        )

