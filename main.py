from V1.py import V1
from V2 import V2

version = input('Deseja iniciar V1 ou V2?')

if version.lower() == 'v1':
    v1 = V1()
    v1.run()
elif version.lower() == 'v2':
    V2.run()
else:
    print ('Versão invalida')