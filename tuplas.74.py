from random import randint
nun = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in nun:
    print(f'{n}', end=' -> ')
print('fim')
print(f'Dos números sorteados, o maior valor foi o {max(nun)}.')
print(f'E o menor valor foi o {min(nun)}.')