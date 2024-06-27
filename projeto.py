N = int(input("digite o numero de vagas: "))
M = int(input("digite quantos clientes estão esperando: "))
lista_vagas = []
ocupadas_count = 0
carros_estacionados = 0
for i in range(M):
    V_i = int(input("digite sua posição: "))
    lista_vagas.append(V_i)
    for j in range(1, V_i + 1):
        if ocupadas_count < N:
            carros_estacionados += 1
            ocupadas_count += 1
            encontrado = True
            break
        else:
            break
print(carros_estacionados)