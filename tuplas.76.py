prod = ('Lápis', 0.50,
        'Borracha', 1.00,
        'Caderno', 10.68,
        'Mochila', 34.90,
        'Livro', 15.00,
        'Caneta', 1.00)

print('{:-^100}'.format(' lista de produtos '))
for item in range(0, len(prod)):
    if item % 2 == 0:
        print(f'{prod[item]:_<30}', end='')
    else:
        print(f'R${prod[item]:>7.2f}')
print('-'*100)
