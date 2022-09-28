lanche = 'Hambúrguer', 'Água', 'Pizza', 'Pudim'
#tuplas são imutáveis
print(lanche)
print('\n')

#print sem as aspas
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Era rodízio, dei prejuízo pro restaurante hehe.')
print('\n')


#print com a contagem de itens
print('Quanto de comida você comeu?')
print(len(lanche))
print('\n')

#contagem em ordem
for contagem in range(0, len(lanche)):
    print(lanche[contagem])
print('\n')

#lanches em ordem alfabética
print(sorted(lanche))
