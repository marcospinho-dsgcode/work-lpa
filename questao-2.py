# Exigência de código 1 de 8
print('Bem-vindo, Marcos Pinho da Silva!')
print('')

# Exigência de código 1 de 8
# Descrição do Menu
print('Preparamos um menu especial com cortes selecionados pensados para agradar todos os paladares, confira as opções:')
print('')
print('------------------------------------------------------')
print('')
print('Bife Acebolado (BA): P = R$ 16 | M = R$ 18 | G = R$ 22')
print('Filé de Frango (FF): P = R$ 15 | M = R$ 17 | G = R$ 21')
print('')
print('------------------------------------------------------')
print('')

# Exigência de código 5 de 8
# Acumulador
total = 0

# Exigência de código 2 de 8 e 7 de 8
# Laço
while True:
    # Colocar o sabor
    sabor = input('Digite o sabor desejado (BA para Bife Acebolado ou FF para Filé de Frango): ')
    
    # Validade do sabor
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido. Tente novamente. ')
        print('')
        continue
        # "continue" para voltar ao início do laço

    # Exigência de código 3 de 8 
    # Entrada do tamanho
    tamanho = input('Digite o tamanho desejado (P, M ou G): ')

    # Verifica se o tamanho é válido
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente. ')
        print('')
        continue
        # "continue" para voltar ao início do laço

 # Exigência de código 4 de 8
 # Verifica o preço com base no sabor e tamanho
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16
        elif tamanho == 'M':
            preco = 18
        else:
            preco = 22
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15
        elif tamanho == 'M':
            preco = 17
        else:
            preco = 21

# Mostrar pedido
    print(f'Pedido: {sabor} tamanho {tamanho} - R$ {preco}')
    print('')

    # Somar o valor ao total
    total += preco

    # Exigência de código 6 de 8 
    resposta = input('Deseja pedir mais alguma coisa? (S para sim / N para não): ')
    
    # Continua apenas se o usuário digitar exatamente "S"
    if resposta != 'S':
        break
        # Para encerrar o laço se a resposta for diferente de S

# Mostra o total final da compra
print(f'\nTotal da sua compra: R$ {total}')
print('Obrigado pela preferência!')

# Exigência 8 de 8 = inserir comentários atendida desde o início do código.