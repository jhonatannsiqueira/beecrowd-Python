#a nota máxima na prova substitutiva é dez e que ela pode substituir apenas a nota da prova regular, não a de trabalhos
nota_de_trabalhos = float(input())
nota_da_prova_regular = float(input())
media_final = (nota_de_trabalhos + nota_da_prova_regular) / 2
if media_final >= 6:
    print('aprovado')
elif media_final < 6 and nota_de_trabalhos >= 2:
    print('talvez com a sub')
else:
    print('reprovado')
