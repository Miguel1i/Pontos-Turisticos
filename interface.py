from pontointeresse import Ponto
from sistema import Sistema
from variable import menu as m


def menu(sistema: Sistema):
    while True:
        print(m)
        ans = str(input('Escolha a opção >> '))
        match ans:
            case '1':
                _id = sistema.get_last_id() + 1
                designacao = str(input("Designacao: "))
                morada = str(input("Morada: "))
                latitude = float(input("Latitude: "))
                longitude = float(input("Longitude: "))
                categoria = str(input("Categoria: "))
                acess = str(input("Acessiblidade: "))
                ponto = Ponto(_id, designacao, morada, latitude, longitude, categoria, acess)
                sistema.adicionar_ponto(ponto)
            case '2':
                sistema.listar_pontos()
                _id = int(input('ID: '))
                categoria = str(input('Categoria: '))
                acess = str(input('Acessibilidade: '))
                sistema.alterar_ponto(_id, categoria, acess)
            case '3':
                categoria = str(input('Categoria: '))
                sistema.pesquisar_pontos(categoria)
            case '4':
                sistema.listar_pontos()
                _id = int(input("id: "))
                avaliacao = int(input("Avalia 1-4: "))
                sistema.assinalar_avaliar_ponto(_id, avaliacao)
            case '5':
                sistema.consultar_estatisticas()
            case '6':
                latitude = float(input('Latitude: '))
                longitude = float(input('Longitude: '))
                sistema.obter_sugestoes(latitude, longitude)
            case '0':
                break
            case _:
                print("Opcao inválida!")
