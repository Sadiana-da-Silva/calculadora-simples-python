"""""
Objetivo do desafio: Desenvolver um aplicativo que gerencie uma lista de compras que permita adicionar, remover e listar os produtos adicionados nela. 

Para isso, o seu aplicativo precisa ter as seguintes funcionalidades: 

Menu de Opções: O sistema deve fornecer um menu de opções para o usuário interagir. As opções devem ser as seguintes:  
1. Adicionar produto 
2. Remover produto  
3. Pesquisar produtos   
s. Sair do programa  
  
Adicionar Produto: O usuário deve poder adicionar um novo produto à lista de compras. O sistema deve solicitar informações sobre o nome, unidade de medida, quantidade e descrição do produto.   
As opções de unidade devem ser:  
- Quilograma  
- Grama  
- Litro  
- Mililitro  
- Unidade  
- Metro  
- Centímetro  
Essas opções devem aparecer quando o sistema perguntar a unidade de medida.
"""""
import unicodedata


def remover_acentos(texto):
    #Normaliza a string e remove caracteres diacríticos (acentos)
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != "Mn")

def lista_de_compras():
    lista_produtos = []

    while True:
        print("Lista de Compras Simples")
        print()
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Pesquisar produtos")
        print("s. Sair do programa")
        opcao = input("Selecione uma opção ou 's' para sair: ")

        if opcao == 's' or opcao == 'S':
            print("Obrigado por utilizar a Lista de Compras Simples!")
            break

        if opcao not in ['1', '2', '3']:
            print("Opção inválida! Tente novamente.")
            continue

        if opcao == '1':
            item_para_adicionar = input("Digite um item para adicionar à lista: ")
            lista_produtos.append(item_para_adicionar)
            print("Item aidicionado com sucesso!")

        elif opcao == '2':
            if not lista_produtos:
                print("A lista está vazia. Não há itens para remover.")
                continue

#Exibir a lista com índices para remoção
            for indice, item in enumerate(lista_produtos):
                print(f"{indice}. {item}")


            try:
                item_para_remover = int(input("Digite o índice do item que deseja remover: "))
                if 0 <= item_para_remover < len(lista_produtos):
                    lista_produtos.pop(item_para_remover)
                    print("Item removido com sucesso!")
                else:
                    print("Índice inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

        elif opcao == '3':
            item_para_pesquisa = input("Digite o nome ou parte do nome do produto que deseja pesquisar: ").lower()
            item_para_pesquisa = remover_acentos(item_para_pesquisa) # Remove acentos do termo de pesquisa

            # Pesquisar removendo acentos dos produtos também
            produtos_encontrados = [produto for produto in lista_produtos if item_para_pesquisa in remover_acentos(produto.lower())]
            if produtos_encontrados:
                print("Produto encontrado: ")
                for produto in produtos_encontrados:
                    print(f"- {produto}")
            else:
                print("Nenhum produto encontrado com esse termo.")

        print("\nLista de Compras Atualizada:")
        for indice, item in enumerate(lista_produtos):
            print(f"{indice}. {item}")
        print()


lista_de_compras()