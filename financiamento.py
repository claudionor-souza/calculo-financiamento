from time import sleep
print('$' * 30)
print('{:^15}'.format('CALCULADOR FINANCIAMENTO'))
print('$' * 30)
salario = float(input('Salário: '))
limite = salario * (30/100)
capital = float(input('Valor a financiar (R$): '))
taxa = float(input('Taxa de juros (%): '))
taxa_i = taxa / 100
periodo = int(input('Período (em meses): '))
total = capital * (1 + taxa_i) ** periodo
montante = total
parcela = montante / periodo

print('Análise de crédito em andamento...')
sleep(4)
print('Finalizando...')
sleep(3)
if limite > parcela:
    print('Parabéns! Seu financiamento foi APROVADO!')
    sleep(2)
    print(f'Valor financiado: R${capital:.2f}')
    print(f'Valor final: R${montante:.2f}')
    print(f'Número de parcelas: {periodo} meses')
    print(f'Valor das parcelas: {parcela:.2f}')
    sleep(3)
    print('FIM DO PROGRAMA')

else:
    print(f'O valor disponível com base nos seus ganhos não foi suficiente')
    print('Infelizmente não foi possível aprovar seu crédito.')
    sleep(3)
    print('FIM DO PROGRAMA')
