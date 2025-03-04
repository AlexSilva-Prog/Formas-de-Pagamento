valor_do_produto = float(input('Digite o valor do produto: '))
pagamento = input('Qual a Forma de pagamento? dinheiro,cheque,cartao debito,cartao credito 2x ou 3x: ')

if pagamento == 'dinheiro' or pagamento == 'cheque':
    desconto_dinheiro = valor_do_produto * (10 / 100)
    valor_final01 = valor_do_produto - desconto_dinheiro
    print(f'Forma de pagamento escolhida: {pagamento}! direito a 10% de desconto')
    print(f'Produto de R${valor_do_produto} Reias por apenas R${valor_final01} Reais')

elif pagamento == 'cartao debito':
    desconto_cartao_debito = valor_do_produto * (5 / 100)
    valor_final02 = valor_do_produto - desconto_cartao_debito
    print(f'Forma de pagamento escolhido: {pagamento}! direto a 5% de desconto')
    print(f'Produto de R${valor_do_produto} Reais por apenas R${valor_final02} Reais')

elif pagamento == 'cartao credito 2x':
    print(f'Forma de pagamento escolhido: {pagamento}')
    parcelas_2x = valor_do_produto / 2
    print(f'Ficando 2x de R${parcelas_2x} Reais')

elif pagamento == 'cartao credito 3x':
    print(f'Forma de pagamento escolhido: {pagamento}')
    juros_parcelando = valor_do_produto * (20 / 100)
    juros_20 = valor_do_produto + juros_parcelando
    parcelas_3x = juros_20 / 3
    print(f'Ficando 3x de R${parcelas_3x} Reais ja somando os "20% de juros"')

else:
    print('\033[1;31mForma de pagamento invalida!\033[m')