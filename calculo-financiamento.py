from time import sleep
print('<*>' * 11)
print('{:^35}'.format('CALCULO DE FINANCIAMENTO'))
print('<*>' * 11)
rendimento = float(input('Valor do rendimento (R$): '))
limite = rendimento * 30 / 100
produto = str(input('Tipo de produto: ')).strip().upper()
valor = float(input('Valor a ser financiado (R$): '))
taxa = float(input('Valor da taxa de juros (%): '))
conversao = taxa / 100
periodo = int(input('Quantidade de meses: '))
juros = (1 + conversao) ** periodo - 1
juros1 = (1 + conversao) ** periodo * conversao
aplicavel = juros / juros1
parcela = valor / aplicavel
total = parcela * periodo
if limite > parcela:
    print('Crédito em análise...')
    sleep(3)
    print('ANÁLISE CONCLUÍDA COM SUCESSO!')
    sleep(1)
    print(f'CRÉDITO APROVADO')
    sleep(1)
    print(f'Tipo de produto: {produto}')
    print(f'Valor do produto: R${valor:.2f}')
    sleep(1)
    print(f'Quantidade de parcelas: {periodo}')
    sleep(1)
    print(f'Valor das parelas: R${parcela:.2f}')
    sleep(1)
    print(f'Valor total do financiamento: R${total:.2f}')
    sleep(2)
    print('FIM DO PROGRAMA')
else:
    print('Crédito em análise...')
    sleep(3)
    print('ANÁLISE CONCLUÍDA')
    sleep(1)
    print(f'INFELIZMENTE O CRÉDITO NÃO FOI APROVADO')
    sleep(2)
    print('FIM DO PROGRAMA')
