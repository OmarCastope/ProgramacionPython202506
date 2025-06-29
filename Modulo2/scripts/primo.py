











# 1. recorro el listado de numeros a evaluar
for numero in listado_numero:
    # 2. encuentro sus divisores
    divisores = []
    for i in range(1, numero+1):
        if numero%i==0:
            divisores.append(i)
    print(f'{numero} -> {divisores}')

print('Fin del programa!')





