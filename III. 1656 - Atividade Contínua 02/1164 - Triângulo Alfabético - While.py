n = int(input())
letra = 'A'
linha = 1

while linha < n+1:
    print(letra * linha)
    letra = chr(ord(letra) + 1)
    linha += 1
