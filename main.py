from sistema import Sistema
from interface import menu
from os import system


def main() -> None:
    """
    Cria uma instância da classe Sistema e chama a função menu() passando essa
    instância como argumento.
    :return: None
    """
    sistema = Sistema()
    system('cls')
    menu(sistema)


if __name__ == '__main__':
    main()
