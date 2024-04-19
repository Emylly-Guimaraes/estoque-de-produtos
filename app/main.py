from utils.registradorEstoque import registradorEstoque
from utils.retornoEstoque import retornoEstoque

def estoque():
    print("Bem-vindo ao sistema de estoque\n")
    
    lista1 = []   

    while True:
        print("Selecione um número de acordo com seu interesse:\n")
        print("1 - Cadastrar novo produto ")
        print("2 - Listar todos os produtos ")
        print("3 - Sair ")
        opcao1 = int(input("Digite o número: "))

        if opcao1 == 3:
            print("Obrigada por usar nosso sistema!")
            return 'Sistema encerrado'
        elif opcao1 == 1:
            nome_do_produto = str(input("Digite o nome do produto: "))
            preco = str(input("Digite o preço do produto: "))
            qtd= str(input("Digite o estoque do produto: "))
            
            dicionario1 = {
                'nome': f'{nome_do_produto}',
                'preco': f'{preco}',
                'quant': f'{qtd}'
            }
            print(lista1)
            lista1 = registradorEstoque(lista1,dicionario1)
            print(lista1)
        
        elif opcao1 == 2:
            print("Produtos cadastrados:")
            retornoEstoque(lista1)
            

print(estoque())


