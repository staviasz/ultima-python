valor_produto = float(input('Digite  o valor do produto: '))
forma_pagamento = str(input('O pagamento será em dinheiro ou cartão: '))

if forma_pagamento == 'dinheiro':
    valor_final = valor_produto - valor_produto * 0.15
    print(f'Pagando á vista em dinheiro há um desconto de 15% resultando no valor final de: {valor_final}')
else:
    parcela = int(input('Quantas parcelas: '))
    if parcela == 1:
        valor_final = valor_produto - valor_produto * 0.10
        print(f'Pagando á vista no catão há um desconto de 10% resultando no valor final de: {valor_final}')
    elif parcela == 2:
        valor_final = valor_produto
        print(f'Pagando em 2x no cartão o valor final é: R${valor_final:.2f}, com a parcela de: R${valor_final/parcela:.2f}')
    else:
        valor_final = valor_produto + valor_produto * 0.10
        print(f'Pagando acima de 2x catão há um juros de 10% resultando no valor final de: R${valor_final:.2f}, com a parcela de: R${valor_final/parcela:.2f}')

