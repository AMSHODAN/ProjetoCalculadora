class V2():
    conta = input('conta? ')
    itens = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             'x': lambda x, y: x * y,
             '/': lambda x, y: x / y}

    indice = None
    for item in itens:
        indice = conta.find(item)
        if indice != -1:
            break

    if indice == -1:
        raise ValueError('Denominador inválido ou ausente!')
    else:
        n1 = int(conta[:indice])
        n2 = int(conta[indice + 1:])
        norm = conta[indice]
        resultado = itens[norm](n1, n2)
        print(resultado)
if __name__ == '__main__':
    V2_local = V2()
    V2_local.run()