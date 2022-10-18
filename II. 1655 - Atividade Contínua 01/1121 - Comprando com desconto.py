preco_mercadoria = float(input())
mercadoria_quantidade = int(input())
sem_desconto = preco_mercadoria * mercadoria_quantidade
desconto10 = 0.10
desconto1 = mercadoria_quantidade * 0.01
desconto_total = sem_desconto * (desconto10 + desconto1)
com_desconto = sem_desconto - desconto_total
print(f'{sem_desconto:.2f}')
print(f'{com_desconto:.2f}')
