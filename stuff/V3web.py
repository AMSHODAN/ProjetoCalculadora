import re

numeros = input('conta?') 
itens = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         'x': lambda x, y: x * y,
         '/': lambda x, y: x / y}
catch = False

def calc():
    separador = re.compile('[0-9] {1,99} [x/+-] [0-9]{1,99}')
    buscador = separador.search(numeros)
    for item in itens:
        indice = numeros.find(item)
        if indice != -1:
            primeiro_numero = numeros[:indice]
            contador = numeros[indice]
            segundo_numero = numeros[indice + 1:]
            return primeiro_numero, contador, segundo_numero
    return None, None, None

primeiro_numero, contador, segundo_numero = calc()

if primeiro_numero is None:
    print("Nenhum caractere encontrado.")
else:
    class conta:
        def __init__(self, primeiro_numero, contador, segundo_numero):
            self.primeiro_numero = primeiro_numero
            self.contador = contador
            self.segundo_numero = segundo_numero

    calculo = conta(primeiro_numero, contador, segundo_numero)
    print(calculo.primeiro_numero)
    print(calculo.contador)
    print(calculo.segundo_numero)
    resultado = itens[contador](primeiro_numero, segundo_numero)
    print(f'o resultado é {resultado}')