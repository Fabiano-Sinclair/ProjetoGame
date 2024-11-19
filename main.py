from Game import Game

def main():
    try:
        # Cria uma instância do jogo
        game = Game()

        # Executa o jogo
        game.run()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        print("Encerrando o jogo...")

if __name__ == '__main__':
    main()


