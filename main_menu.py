import pygame
from Level import run_game  # Importa a função do jogo

class MainMenu:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.running = True
        self.background = pygame.image.load('./asset/War.png')
        self.background = pygame.transform.scale(self.background, (self.window.get_width(), self.window.get_height()))
        self.title = "Brutal War"
        self.title_color = (255, 0, 0)
        self.title_size = 100
        self.options = ["Iniciar Jogo", "Configurações", "Sair"]
        self.option_color = (255, 255, 255)
        self.option_selected_color = (255, 0, 0)
        self.option_size = 50
        self.option_spacing = 40
        self.current_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)
                elif event.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.current_option == 0:  # "Iniciar Jogo"
            pygame.mixer_music.stop()
            self.running = False
            run_game()  # Chama o jogo diretamente
        elif self.current_option == 1:  # "Configurações"
            print("Abrir Configurações (em construção).")
        elif self.current_option == 2:  # "Sair"
            self.running = False
            pygame.quit()

    def draw(self):
        self.window.blit(self.background, (0, 0))
        title_y_pos = self.window.get_height() // 4
        self.menu_text(font_size=self.title_size, text=self.title, text_color=self.title_color,
                       text_center_pos=(self.window.get_width() // 2, title_y_pos))
        start_y_pos = self.window.get_height() // 2
        for i, option in enumerate(self.options):
            color = self.option_selected_color if i == self.current_option else self.option_color
            option_y_pos = start_y_pos + i * (self.option_size + self.option_spacing)
            self.menu_text(font_size=self.option_size, text=option, text_color=color,
                           text_center_pos=(self.window.get_width() // 2, option_y_pos))
        pygame.display.flip()

    def menu_text(self, font_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(text_surface, text_rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menu Principal")
    menu = MainMenu(window)
    menu.run()
    pygame.quit()
