words = 'aprender', 'estudar', 'programar', 'curso', 'python', 'javascript', 'trabalho', 'carreira', 'futuro', 'mercado', 'aulas', 'prática'

for w in words:
    print(f'\nNa palavra {w.upper()} temos ', end='')
    for letra in w:
        if letra.lower() in 'aáàâãéeioõu':
            print(letra, end=' ')