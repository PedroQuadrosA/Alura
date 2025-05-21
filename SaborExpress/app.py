import os

#criando uma lista global
restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, # 'nome' = chave: 'Praça' = valor
                {'nome': 'Cassarolas do Cassiano', 'categoria': 'Francesa', 'ativo': True},
                {'nome': 'Churrasco do Campos', 'categoria': 'Gaudéria', 'ativo': False}]

def exibir_nome_programa():
    print("""
      
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
      """)
    
def exibir_opcoes():    
    print('########################')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')
    print('########################')

# a função é um bloco de código que vai realizar uma ação
def finalizar_app():
    exibir_subtitulo('Finalizando o Programa.')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar para o menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida.\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print('########################')
    print(texto)
    print('########################')
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrando Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    #restaurantes.append(nome_do_restaurante) #append é igual ao push javascript
    #aqui criamos um dicionário pra criação de um novo restaurante no esquema de chave e valor
    dados_do_restaurante = {'nome': nome_do_restaurante, 
                            'categoria': categoria,
                            'ativo': False}
    restaurantes.append(dados_do_restaurante) # e aqui adicionamos ele para a lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'- {nome_restaurante} | Categoria: {categoria_restaurante} | Status: {ativo_restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    # opcao_escolhida = int(input('\nEscolha uma opção: '))
    # try:
    #     match opcao_escolhida:
    #         case 1:
    #             print('Cadastrar Restaurante.')
    #         case 2:
    #             print('Listar Restaurantes.')
    #         case 3:
    #             print('Ativar Restaurante.')
    #         case 4:
    #             finalizar_app()
    #         case _:
    #             opcao_invalida()
    # except :
    #     opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
