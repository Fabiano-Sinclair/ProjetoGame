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

        # Carrega a imagem de fundo e redimensiona para o tamanho da janela
        self.background = pygame.image.load('./asset/War.png')
        self.background = pygame.transform.scale(self.background, (self.window.get_width(), self.window.get_height()))

        # Configurações do menu
        self.title = "Brutal War"  # Título do menu
        self.title_color = (255, 0, 0)
        self.title_size = 100

        self.options = ["Iniciar Jogo", "Configurações", "Sair"]  # Opções do menu
        self.option_color = (255, 255, 255)
        self.option_selected_color = (255, 0, 0)
        self.option_size = 50
        self.option_spacing = 40  # Espaçamento vertical entre as opções
        self.current_option = 0  # Índice da opção selecionada

        # Música de fundo
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

    def handle_events(self):
        """
        Trata os eventos do menu.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Encerra o menu
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)  # Vai para a próxima opção
                elif event.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)  # Vai para a opção anterior
                elif event.key == pygame.K_RETURN:
                    self.select_option()  # Seleciona a opção atual

    def select_option(self):
        """
        Ação ao selecionar uma opção no menu.
        """
        if self.current_option == 0:  # "Iniciar Jogo"
            self.running = False
        elif self.current_option == 1:  # "Configurações"
            print("Abrir Configurações (em construção).")
        elif self.current_option == 2:  # "Sair"
            self.running = False
            pygame.quit()

    def menu_text(self, font_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """
        Renderiza texto como imagem e o desenha na tela.
        :param font_size: Tamanho da fonte do texto.
        :param text: O texto a ser renderizado.
        :param text_color: A cor do texto (tupla RGB).
        :param text_center_pos: A posição central do texto na tela (x, y).
        """
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(text_surface, text_rect)

    def draw(self):
        """
        Desenha a tela do menu.
        """
        # Preencher o fundo com a imagem
        self.window.blit(self.background, (0, 0))

        # Exibir o título do menu
        title_y_pos = self.window.get_height() // 4  # Título fica a 1/4 da altura da tela
        self.menu_text(font_size=self.title_size, text=self.title, text_color=self.title_color,
                       text_center_pos=(self.window.get_width() // 2, title_y_pos))

        # Exibir as opções do menu
        start_y_pos = self.window.get_height() // 2  # Primeira opção começa no meio da tela
        for i, option in enumerate(self.options):
            color = self.option_selected_color if i == self.current_option else self.option_color
            option_y_pos = start_y_pos + i * (self.option_size + self.option_spacing)
            self.menu_text(font_size=self.option_size, text=option, text_color=color,
                           text_center_pos=(self.window.get_width() // 2, option_y_pos))

        # Atualizar a tela
        pygame.display.flip()

    def run(self):
        """
        Executa o menu principal.
        """
        while self.running:
            self.handle_events()  # Verifica eventos
            self.draw()  # Renderiza o menu
