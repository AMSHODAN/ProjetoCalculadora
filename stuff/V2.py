class V2():
    repetição = True
    while repetição:
        conta = int(input('conta? 00 para fechar'))
        complexo = int(input('Ver como chegamos ao resultado? [1 para sim] e [2 para não]'))
        itens = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 'x': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
        
        if conta == 00:
            print ('fechando...')
            break
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
            if complexo == 1:
                
                print(resultado)
            elif complexo == 0:
                print(resultado)
if __name__ == '__main__':
    V2_local = V2()
    V2_local.run()