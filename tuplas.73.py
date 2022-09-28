print('{:-^100}'.format(' campeonato brasileiro de futebol '))

jogadoras = 'Maria', 'Karen', 'Paula', 'Marina', 'Amanda', 'Eduarda', 'Rebeka', 'Ludmilla', 'Julia', 'Gabriela', 'Lara', 'Beatriz', 'Clara', 'Joana', 'Bruna', 'Eni', 'Fernanda', 'Luiza', 'Luana', 'Milena'

# a)
print('As 5 primeiras colocadas foram:')
for contagem in range(0, len(jogadoras[0:5])):
    print(jogadoras[contagem])

#b)
print('='*100)
print('As últimas 4 colocadas foram:')
for contagem in range(16, len(jogadoras[:20])):
    print(jogadoras[contagem])

#c)
print('='*100)
print('Todas as jogadoras em ordem alfabética:')
print(sorted(jogadoras))

#d)
print('='*100)
print('A posição que a jogara Clara está é de:')
print(jogadoras.index('Clara'))

