# Exigência de código 1 de 7
print("Olá, Marcos Pinho da Silva!")
print("Bem-vindo ao sistema online da loja de fábrica Organic Clothes")
print('')
print('_'*40)
print('')

# Exigência de código 2 de 7
def escolha_modelo():
    while True:
        print("\nEscolha o modelo desejado:")
        print("MCS = Manga Curta Simples: R$1.80")
        print("MLS = Manga Longa Simples: R$2.10")
        print("MCE = Manga Curta com Estampa: R$2.90")
        print("MLE = Manga Longa com Estampa: R$3.20")
        print('')
        modelo = input("Digite o código do modelo: ")

        if modelo == "MCS" or modelo == "mcs":
            return 1.80
        elif modelo == "MLS" or modelo == "mls":
            return 2.10
        elif modelo == "MCE" or modelo == "mce":
            return 2.90
        elif modelo == "MLE" or modelo == "mle":
            return 3.20
        else:
            print("Opção inválida. Por favor, digite um dos códigos válidos.")

# Exigência de código 3 de 7
def num_camisetas():
    while True:
        try:
            quantidade = int(input("\nDigite o número de camisetas desejado: "))

            if quantidade > 20000:
                print("Não aceitamos pedidos com mais de 20.000 camisetas.")
            elif quantidade >= 2000:
                return quantidade * 0.88  # Desconto de 12%
            elif quantidade >= 200:
                return quantidade * 0.93  # Desconto de 7%
            elif quantidade >= 20:
                return quantidade * 0.95  # Desconto de 5%
            elif quantidade > 0:
                return quantidade  # Sem desconto
            else:
                print("Digite um número positivo de camisetas.")
        except ValueError:
            print("Erro: Digite um número inteiro.")

# Exigência de código 4 de 7
def frete():
    while True:
        print("\nEscolha o tipo de frete:")
        print("0 = Retirar na fábrica R$0")
        print("1 = Transportadora R$100")
        print("2 = Sedex R$200")
        tipo_frete = input("Digite a opção de frete (0, 1 ou 2): ")

        if tipo_frete == "0":
            return 0
        elif tipo_frete == "1":
            return 100
        elif tipo_frete == "2":
            return 200
        else:
            print("Opção de frete inválida. Tente novamente.")

# Exigência de código 5 de 7 e 6 de 7
# Aqui inicia (main) o código principal
try:
# Perguntar e retornar valor do modelo
    valor_unitario = escolha_modelo()
# Perguntar quantidade e aplicar desconto
    quantidade_descontada = num_camisetas()
# Perguntar e retornar valor do frete
    valor_frete = frete()

    # Calcula o valor total
    total = (valor_unitario * quantidade_descontada) + valor_frete

    # Exibe o resultado final
    print("\nResumo do pedido:")
    print("Valor das camisetas com desconto: R${:.2f}".format(valor_unitario * quantidade_descontada))
    print("Valor do frete: R${:.2f}".format(valor_frete))
    print("Valor total a pagar: R${:.2f}".format(total))

except Exception as e:
    print("Ocorreu um erro inesperado:", e)

# Exigência de código 7 de 7 = inserir comentários atendida desde o início do código.