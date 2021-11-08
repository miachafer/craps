"""
Jogo de craps:
Faça um programa que implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira rodada, você fez um 4, 5, 6, 8, 9 ou 10, este é o seu ponto.
Seu objetivo agora é continuar jogando os dados até tirar este ponto novamente.
Você perde no entanto, se tirar um 7 antes de tirar este número novamente.
"""

### JOGO DE CRAPS 


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

