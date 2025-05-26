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
    print('3. Trocar Status do Restaurante')
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
    linha = '#' * (len(texto))
    print(linha)
    print(texto)
    print(linha)    
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
    print(f'{'Nome do Restaurante'.ljust(24)} | {'Categoria'.ljust(33)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(22)} | Categoria: {categoria_restaurante.ljust(22)} | Status: {ativo_restaurante}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Mudando o Estado do Restaurante')
    nome_restaurante = input('Digite o nome do Restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi atiavado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')
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
            alternar_estado_restaurante()
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
