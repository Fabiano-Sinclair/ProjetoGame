import pygame
from Menu import Menu

# Classe do jogo principal
class Game:
    def __init__(self, levels: list = None):
        """
        Inicializa o jogo com uma lista de níveis.
        :param levels: Lista de instâncias da classe Level (opcional).
        """
        pygame.init()

        # Altera o tamanho da janela para o tamanho da imagem
        self.window = pygame.display.set_mode(size=(1920, 1080))
        pygame.display.set_caption('Jogo Principal')

        self.levels = levels if levels else []
        self.current_level_index = 0
        self.running = True

    def handle_events(self):
        """
        Trata eventos do Pygame.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):

        """
        Executa o jogo.
        """
        print('Game Started')

        # Inicializa o menu
        menu = Menu(self.window, self)  # Passa a instância do jogo para o menu
        menu.run()  # Executa o menu antes do jogo começar

        # Loop principal do jogo
        while self.running:
            self.handle_events()

            # Fundo simples (preto) enquanto não há níveis
            self.window.fill((0, 0, 0))  # Preenche a tela com preto
            pygame.display.flip()  # Atualiza a janela

        pygame.quit()  # Encerra o Pygame
        print('Game Closed')
