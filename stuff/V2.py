conta = input('conta?')
itens = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         'x': lambda x, y: x * y,
         '/': lambda x, y: x / y}
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
    resultado = itens[item](n1, n2)
    print(resultado)