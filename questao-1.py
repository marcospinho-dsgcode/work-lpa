# Exigência de código 1 de 6
print('Bem-vindo Marcos Pinho da Silva!')

# Exigência de código 2 de 6
# O usuário insere o valor do pedido e a quantidade de parcelas
ValorDoPedido = float(input('Digite o valor do pedido: '))
QuantidadeParcelas = int(input('Digite a quantidade de parcelas: '))

# Para o valor do juros iniciar em 0
juros = 0

# Exigência de código 3 de 6 e 5 de 6
# Implementação dos juros considerando condições de menor, igual e maior
if QuantidadeParcelas < 4:
    juros = 0
elif QuantidadeParcelas >= 4 and QuantidadeParcelas < 6:
    juros = 0.04
elif QuantidadeParcelas >= 6 and QuantidadeParcelas < 9:
    juros = 0.08
elif QuantidadeParcelas >= 9 and QuantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32

# Exigência de código 4 de 6
# Para calcular o valor de cada parcela
ValorDaParcela = (ValorDoPedido * (1 + juros)) / QuantidadeParcelas
# Para calcular o valor total com juros
ValorTotalParcelado = ValorDaParcela * QuantidadeParcelas

# Exibição do valor de cada parcela
print("Valor de cada parcela: R$", ValorDaParcela)

# Exibição do valor total a ser pago
print("Valor total a pagar: R$", ValorTotalParcelado)

# Exigência 6 de 6 = inserir comentários atendida desde o início do código.