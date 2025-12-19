
lista = []
with open('input.txt', 'r') as arquivo:
    for linha in arquivo:
        entrada = linha.strip()

        lista2 = []
        tamanho = len(entrada)

        for i in range(0, tamanho):
            first = entrada[i]
            for j in range(i + 1, tamanho):
                num = entrada[j]
                conca = int(first + num)
                lista2.append(conca)
        if lista2:
            lista.append(max(lista2))

print(sum(lista))