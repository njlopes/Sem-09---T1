contador_pares = 0
contador_impares = 0

for i in range(100):
    numero = int(input('Digite um valor:'))

    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print('A quantidade de números pares é igual a:',contador_pares)
print('A quantidade de números ímpares é igual a:',contador_impares)

