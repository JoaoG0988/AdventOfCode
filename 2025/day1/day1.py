pos = 50
cont = 0

while True:
    entrada = input()
    move = entrada[0]
    passos = int(entrada[1:])

    if move == "R":
        cont += (pos + passos) // 100
        pos = (pos+passos) % 100
    elif move == "L":
        dist_ate_zero = (100 - pos) % 100
        cont += (dist_ate_zero + passos) // 100
        pos = (pos-passos) % 100
    print(cont)

