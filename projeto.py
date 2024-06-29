N = int(input("digite o numero de vagas: "))
while N < 1 or N > 100000:
    print("valor invalido. Tente de novo")
    N = int(input("digite o numero de vagas: "))
M = int(input("digite quantos clientes estão esperando: "))
while M < 1 or M > 100000:
    print("valor invalido. Tente de novo")
    M = int(input("digite quantos clientes estão esperando: "))
lista_vagas = []
carros_estacionados = 0
for i in range(M):
    V_i = int(input("digite sua posição: "))
    while V_i > N or V_i < 1:
        print("vaga invalida. Tente de novo")
        V_i = int(input("digite sua posição: "))
    if V_i in lista_vagas:
        while V_i in lista_vagas:
            V_i -=1
        lista_vagas.append(V_i)
        carros_estacionados += 1
        if V_i == 0:
                del(lista_vagas[i])
                carros_estacionados -= 1
                print(f"Carros estacionados: {carros_estacionados}")
                exit()
    else:
        lista_vagas.append(V_i)
        carros_estacionados += 1
print(f"Carros estacionados: {carros_estacionados}")