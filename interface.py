from sistema import Sistema
from variable import menu as m


def menu(sistema: Sistema):
    while True:
        print(m)
        ans = str(input('Escolha a opção >> '))
        match ans:
            case '1':
                sistema.adicionar_ponto()
            case '2':\
                sistema.alterar_ponto()
            case '3':
                sistema.pesquisar_pontos()
            case '4':
                sistema.assinalar_avaliar_ponto()
            case '5':
                sistema.consultar_estatisticas()
            case '6':
                sistema.obter_sugestoes()
            case '0':
                break
            case _:
                print("Opcao inválida!")
