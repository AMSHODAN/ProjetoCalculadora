class V1():
    repetição = True

    while repetição:
        print('Que tipo de conta quer fazer hoje, meu compatriarcado?')
        TipoConta = int(input('(1)adição (2)subtração (3)multiplicação (4)divisão (0) fechar'))
        fixcomp = input('Quer ver como chegamos ao resultado, me sumonado? [Sim] ou [Não]')
        complexo = fixcomp.lower()

        if TipoConta == 1:
            print('-----------------------------------------Adição selecionada!---------------------------------------------------------')
            adição1 = int(input('Manda o primeiro numero, meu configurado!'))
            adição2 = int(input('Manda o segundo numero, meu consignado!'))
            resultadoadc = adição1 + adição2
            resultadoadccomp = adição1
            if complexo.lower() == 'sim' or 's':
                while resultadoadccomp < resultadoadc:
                    resultadoadccomp = resultadoadccomp + 1
                    print (resultadoadccomp)
                print(f'O resultado é {resultadoadc} meu marcado!')


        elif TipoConta == 2:
            print('---------------------------------------Subtração selecionada!-------------------------------------------------------')
            sub1 = int(input('Manda o primeiro numero, meu conhecedor!'))
            sub2 = int(input('Manda o segundo numero, meu gestor!'))
            resultadosub = sub1 - sub2
            resultadosubcomp = sub1
            if complexo.lower() == 'sim' or 's':
                while resultadosubcomp > resultadosub:
                    resultadosubcomp = resultadosubcomp - 1
                    print (resultadosubcomp)
            print(f'O resultado é {resultadosub} meu campeão!')
            


        elif TipoConta == 3:

            print('------------------------------------------Multiplicação selecionada!-----------------------------------------------------')
            multi1 = int(input('Manda o multiplicado, meu patrão!'))
            multi2 = int(input('Manda o multiplicador, meu professor!'))
            resultadomulti = multi1 * multi2
            resultadomulticomp = multi1
            if complexo.lower() == 'sim' or 's':
                while resultadomulticomp < resultadomulti:
                    resultadomulticomp = resultadomulticomp + multi1
                    print (resultadomulticomp)
            print(f'O resultado é {resultadomulti} meu encontrado!')

        elif TipoConta == 4:

            print('----------------------------------------Divisão selecionada!-------------------------------------------------------------')
            div1 = int(input('Manda o numero a ser dividio, meu marcante!'))
            div2 = int(input('Manda o numero a dividir por, meu achante!'))
            resultadodiv = div1 / div2
            print(f'O resultado é {resultadodiv} meu mandante!')

        elif TipoConta == 0:
            repetição = False
            break

        else:
            print('Numero invalido:( perdeu os oculos de leitura, caixonte?')
            print('Vamos tentar de novo!')
            repetiçãover = int(input('[1]para repetir, qualquer outra coisa para desistir'))
            if repetiçãover == 1:
                print('repetindo...')
            else:
                repetição = False
if __name__ == '__main__':
    V1_local = V1()
    V1_local.run()