print('='*100)
nun = (int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: ')))
print('='*100)

print(f'Você digitou os valores {nun}.')
print('='*100)

#a)
print(f'O valor 9 apareceu {nun.count(9)} vezes.')
print('='*100)

#b)
if 3 in nun:
    print(f'O primeiro valor 3 foi digitado na {nun.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhum momento.')
print('='*100)

#c)
print('Os valores pares digitados foram: ', end='')
for n in nun:
    if n % 2 == 0:
        print(n, end=' -> ')
print('fim')
print('='*100)
