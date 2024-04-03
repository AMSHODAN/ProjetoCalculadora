conta = input('conta?')
itens = ['+', '-', 'x','/']
catch = False

for item in itens:
    indice = conta.find(item)
    if indice != -1:
        break

if indice == -1:
    raise ValueError('Denominador invalido ou ausente!')
else:
    n1 = conta[:indice]
    n2 = conta[indice +1:]
    norm = conta[indice]
    print (n1)
    print (n2)
    print (norm)