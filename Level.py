import pygame
import random

def run_game():
    """
    Executa o jogo de tiro.
    """
    # Inicialização do Pygame
    pygame.init()

    # Configurações da tela
    LARGURA, ALTURA = 800, 600
    TELA = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo de Tiro")

    # Cores
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    VERMELHO = (255, 0, 0)
    AZUL = (0, 0, 255)

    # Classes
    class Jogador(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill(AZUL)
            self.rect = self.image.get_rect(center=(LARGURA // 2, ALTURA - 60))
            self.velocidade = 5

        def update(self):
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.velocidade
            if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA:
                self.rect.x += self.velocidade

        def atirar(self):
            bala = Bala(self.rect.centerx, self.rect.top)
            return bala

    class Inimigo(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill(VERMELHO)
            self.rect = self.image.get_rect(
                center=(random.randint(50, LARGURA - 50), random.randint(-100, -40))
            )
            self.velocidade = random.randint(2, 5)

        def update(self):
            self.rect.y += self.velocidade
            if self.rect.top > ALTURA:
                self.rect.center = (random.randint(50, LARGURA - 50), random.randint(-100, -40))

    class Bala(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((5, 10))
            self.image.fill(VERMELHO)
            self.rect = self.image.get_rect(center=(x, y))
            self.velocidade = -7

        def update(self):
            self.rect.y += self.velocidade
            if self.rect.bottom < 0:
                self.kill()

    # Inicialização dos grupos de sprites
    jogador = Jogador()
    jogador_grupo = pygame.sprite.GroupSingle(jogador)

    balas = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()

    # Gerar inimigos
    for _ in range(5):
        inimigo = Inimigo()
        inimigos.add(inimigo)

    # Loop principal
    rodando = True
    relogio = pygame.time.Clock()

    while rodando:
        relogio.tick(60)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                bala = jogador.atirar()
                balas.add(bala)

        # Atualização
        jogador_grupo.update()
        balas.update()
        inimigos.update()

        # Colisões
        acertos = pygame.sprite.groupcollide(balas, inimigos, True, True)
        for _ in acertos:
            novo_inimigo = Inimigo()
            inimigos.add(novo_inimigo)

        # Desenho na tela
        TELA.fill(PRETO)
        jogador_grupo.draw(TELA)
        balas.draw(TELA)
        inimigos.draw(TELA)

        pygame.display.flip()

    pygame.quit()
