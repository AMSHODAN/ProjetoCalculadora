from flask import Flask, render_template, request #antes colocar no console pip install flask==2.0.2 para funcionar
import re

app = Flask(__name__)

@app.route('/home')
def v3():
    numeros = request.form['conta_info'] 
    itens = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 'x': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    catch = False

    def calc():
        separador = re.compile('[0-9] {1,99} [x/+-] [0-9]{1,99}') #verifica se o input contém uma conta, impedindo que [abcdef5ghijkl-mnop2] seja usado pelo código
        buscador = separador.search(numeros)
        if buscador == -1:
            print ('conta invalida')
            catch = True
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
        resultado = itens[contador](int(primeiro_numero), int(segundo_numero))
        return render_template('v3submittest.html', resultados=resultado)

V3_local = v3()
V3_local.run()
