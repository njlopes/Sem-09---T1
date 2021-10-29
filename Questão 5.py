lista = []
maior = 0
for c in range(100):
    lista.append(int(input()))
    if c == 0:
        maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]

print(f'Dentre os valores digitados o maior é: {maior}')
