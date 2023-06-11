texto = input('Digite um texto: ')
pontuacao = ['.', ',', ';', ':', '!', '?']

for p in pontuacao:
    texto = texto.replace(p, ' ')

texto = texto.split()
print(f'Número de palavras = {len(texto)}')
