num = int(input())
if num % 2 == 0:
    num_impar_antecede = num - 1
    num_par_sucede = num + 2
else:
    num_impar_antecede = num - 2
    num_par_sucede = num + 1
print(num_impar_antecede, num_par_sucede)
