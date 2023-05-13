import os

from pontointeresse import Ponto
from sistema import Sistema
from variable import menu as m


def menu(sistema: Sistema):
    while True:
        print(m)
        ans = str(input('Escolha a opção >> '))
        os.system('clear')
        match ans:
            case '1':
                """
                Adicionar pontos de interesse
                """
                _id = sistema.get_last_id() + 1
                designacao: str = str(input("Designacao: "))
                morada: str = str(input("Morada: "))
                latitude: float = float(input("Latitude: "))
                longitude: float = float(input("Longitude: "))
                categoria: str = str(input("Categoria: "))
                acess: str = str(input("Acessiblidade: "))
                geo: str = str(input("Geografica:"))
                suges: str = str(input("Sugestoes: "))
                ponto: Ponto = Ponto(_id, designacao.strip(), morada.strip(), latitude, longitude, categoria.strip(), [acess], 0, [], [geo],
                                     [suges])
                sistema.adicionar_ponto(ponto)
                os.system("clear")
            case '2':
                '''
                Lista os pontos existentes, pede ao utilizador um id a alterar e faz as alterações
                '''
                sistema.listar_pontos()
                _id: int = int(input('ID: '))
                categoria: str = str(input('Categoria: '))
                acess: str = str(input('Acessibilidade: '))
                sistema.alterar_ponto(_id, categoria, acess)
                os.system("clear")
            case '3':
                '''
                Mostra pontos de interesse por certo tipo de categoria
                '''
                categoria: str = str(input('Categoria: '))
                sistema.pesquisar_pontos(categoria)
            case '4':
                '''
                Pede um id ao utlizador e avalia um ponto de interesse
                '''
                sistema.listar_pontos()
                _id: int = int(input("id: "))
                avaliacao: int = int(input("Avalia 1-4: "))
                while avaliacao < 1 or avaliacao > 4:
                    avaliacao: int = int(input("Avalia 1-4: "))
                sistema.assinalar_avaliar_ponto(_id, avaliacao)
            case '5':
                '''
                Mostra as estatisticas de todos os pontos de interesse
                Visitas, Media de avaliação, Morada e designação
                '''
                os.system("clear")
                sistema.consultar_estatisticas()
            case '6':
                '''
                Calcula pontos de interesses perto atraves de uma localização
                '''
                latitude: float = float(input('Latitude: '))
                longitude: float = float(input('Longitude: '))
                sistema.obter_sugestoes(latitude, longitude)
            case '0':
                '''
                Grava as alterações no json ao sair
                '''
                sistema.grava()
                break
            case _:
                print("Opcao inválida!")
