import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
    """
    Exibe o nome do programa.

    Inputs: None
    Outputs: None
    """
    print("""...""")

def exibir_opcoes():
    """
    Exibe as opções de seleção.

    Inputs: None
    Outputs: None
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Finaliza o app.

    Inputs: None
    Outputs: None
    """
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    """
    Retorna ao menu principal.

    Inputs: None
    Outputs: None
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    """
    Avisa caso o usuário tenha digitado uma opção inválida e retorna ao menu principal.

    Inputs: None
    Outputs: None
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """
    Exibe o subtítulo de cada página.

    Inputs: texto (str) - O subtítulo a ser exibido.
    Outputs: None
    """
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante.

    Inputs: None
    Outputs: None
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista os restaurantes cadastrados.

    Inputs: None
    Outputs: None
    """
    exibir_subtitulo('Listando restaurantes')
    print(f'{"Nome do restaurante".ljust(22)} |  {"Categoria".ljust(20)} | {"Status".ljust(7)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Altera o status dos restaurantes cadastrados.

    Inputs: None
    Outputs: None
    """
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Permite que o usuário escolha uma opção para avançar.

    Inputs: None
    Outputs: None
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

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

def main():
    """
    Função principal do programa.

    Inputs: None
    Outputs: None
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()