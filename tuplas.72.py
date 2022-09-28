#não foi usado tupla

from num2words import num2words

while True:
    nun = int(input('Digite um número de 0 a 20: '))
    if nun > 20:
        print('Erro. Digite apenas um número de 0 a 20')
    elif nun < 0:
        print('Erro. Digite apenas um número de 0 a 20')
    else:
        nunext = num2words(nun, lang='pt-br')
        print(f'Você escolheu o número {nunext}')
        break