import pygame

class Menu:
    def __init__(self, window: pygame.Surface, game):
        """
        Inicializa o menu principal.
        :param window: Janela principal (pygame.Surface).
        :param game: Instância do jogo principal (classe Game).
        """
        self.window = window
        self.game = game
        self.running = True

    def handle_events(self):
        """
        Trata os eventos do menu.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Encerra o menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.running = False  # Fecha o menu para iniciar o jogo

    def draw(self):
        """
        Desenha a tela do menu.
        """
        # Preencher o fundo de preto
        self.window.fill((0, 0, 0))

        # Renderizar o texto
        font = pygame.font.Font(None, 74)
        text = font.render("Pressione Enter para Jogar", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))

        # Exibir o texto
        self.window.blit(text, text_rect)
        pygame.display.flip()

    def run(self):
        """
        Executa o menu principal.
        """
        while self.running:
            self.handle_events()  # Verifica eventos
            self.draw()  # Renderiza o menu
