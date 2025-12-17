entrada = input().split(",")
lista = []
for i in entrada:
    lista.append(i)

soma = 0
numeros_invalidos = []

for i in lista:
    parts = [p.strip() for p in i.split("-") if p.strip()]
    num1,num2 = map(int, parts)

    for numero in range(num1, num2+1):
        tam = len(str(numero))
        if tam % 2 == 0:
            metade = tam // 2
            primeira_metade = str(numero)[:metade]
            segunda_metade = str(numero)[metade:]

            if primeira_metade == segunda_metade:
                numeros_invalidos.append(numero)
        for i in range(1,tam):
            if tam % i == 0:
                sequencia = str(numero)[:i]
                if sequencia * (tam//i) == str(numero) and numero not in numeros_invalidos:
                    numeros_invalidos.append(numero)


    soma = sum(numeros_invalidos)

print(soma)