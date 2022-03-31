from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)
soma = dado1 + dado2

if soma in [2, 3, 12]:
    print('dado 1:', dado1)
    print('dado 2:', dado2)
    print('soma:', soma)
    print('craps, perdeu')
elif soma in [4, 5, 6, 8, 9, 10]:
    print('dado 1:', dado1)
    print('dado 2:', dado2)
    print('soma:', soma)
    print('ponto:', soma)
    objetivo = soma
    input('jogue os dados novamente')
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2
    print('dado 1:', dado1)
    print('dado 2:', dado2)
    print('soma:', soma)
    while soma != objetivo and soma != 7:
        input('jogue os dados novamente')
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        soma = dado1 + dado2
        print('dado 1:', dado1)
        print('dado 2:', dado2)
        print('soma:', soma)
    if soma == objetivo:
        print('você ganhou')
    else:
        print('você tirou 7 e perdeu')
        exit()
else:
    if soma == 7:
        print('dado 1:', dado1)
        print('dado 2:', dado2)
        print('soma:', soma)
        print('natural! você tirou 7 e ganhou.')
    else:
        print('dado 1:', dado1)
        print('dado 2:', dado2)
        print('soma:', soma)
        print('natural! você tirou 11 e ganhou.')

