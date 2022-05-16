from dados import dadosn
from dados import earth_radius as re
from funcoes import *
from strings import *

print(intro)

stop = False
while stop == False:

    pais_sorteado = sorteia_pais(dadosn)
    end = False
    chances = 20
    lpd = []
    lpds = ''
#print(pais_sorteado)

    print(chamada+comandos)


    while end == False and chances > 0:

        palpite = input('Qual seu palpite? ').lower()
        em_lpd = esta_na_lista(palpite, lpd)

        if palpite == 'dicas' or palpite == 'dica':
            ddisponiveis = ''
            if chances < 4 and dica1 in lddisponiveis:
                lddisponiveis.remove(dica1)
            if chances < 5 and dica2 in lddisponiveis:
                lddisponiveis.remove(dica2)
            if chances < 6 and dica3 in lddisponiveis:
                lddisponiveis.remove(dica3)
            if chances < 7 and dica4 in lddisponiveis:
                lddisponiveis.remove(dica4)
            if chances < 8 and dica5 in lddisponiveis:
                lddisponiveis.remove(dica5)
            for i in range(0, len(lddisponiveis)):
                ddisponiveis += lddisponiveis[i]
            print(dicaspadrao+ddisponiveis)
            escolhavalida = False
            while escolhavalida == False:
                if lddisponiveis == []:
                    print('\033[0;31;40mDesculpe, não há mais dicas disponíveis! Digite 0 e retorne aos palpites\n\033[0;0;40m')
                escolha = input('\nDigite o número da dica escolhida: ')
                if escolha == '1' and dica1 in lddisponiveis:
                    letra_sorteada = sorteia_letra(dadosn[pais_sorteado]['capital'], letras_compradas)
                    letras_compradas.append(letra_sorteada)
                    escolhad1 = '  - Letras da capital: '
                    for i in range(0,len(letras_compradas)):
                        if i == 0:
                            escolhad1 += '{}'.format(letras_compradas[i])
                        else:
                            escolhad1 += ', {}'.format(letras_compradas[i])
                    if sorteia_letra(dadosn[pais_sorteado]['capital'], letras_compradas) == '':
                        lddisponiveis.remove(dica1)
                    escolhad1 += '\n'
                    descolhidas[0] = escolhad1
                    chances -= 3
                    escolhavalida = True
                elif escolha == '2' and dica2 in lddisponiveis:
                    cores_bandeira = lista_bandeira(dadosn, pais_sorteado)
                    for i in range(0, len(cores_bandeira)):
                        if len(descolhidas[1]) == 0: 
                            cores = '  - Cores da bandeira: {}'.format(cores_bandeira[i])
                            break
                        elif cores_bandeira[i] not in descolhidas[1]:
                            cores += ', {}'.format(cores_bandeira[i])
                            cores_bandeira.remove(cores_bandeira[i])
                            break
                    if cores_bandeira == []:
                        lddisponiveis.remove(dica2)
                    descolhidas[1] = cores + '\n'
                    chances -= 4
                    escolhavalida = True
                elif escolha == '3' and dica3 in lddisponiveis:
                    descolhidas[2] += '  - População: {} habitantes\n'.format(dadosn[pais_sorteado]['populacao'])
                    lddisponiveis.remove(dica3)
                    chances -= 5
                    escolhavalida = True
                elif escolha == '4' and dica4 in lddisponiveis:
                    descolhidas[3] = '  - Área: {} km2\n'.format(dadosn[pais_sorteado]['area'])
                    lddisponiveis.remove(dica4)
                    chances -= 6
                    escolhavalida = True
                elif escolha == '5' and dica5 in lddisponiveis:
                    descolhidas[4] = '  - Continente: {}\n'.format(dadosn[pais_sorteado]['continente'])
                    lddisponiveis.remove(dica5)
                    chances -= 7
                    escolhavalida = True
                elif escolha == '0':
                    escolhavalida = True
                else:
                    print('\033[0;31;40m\nOpção inválida!\033[0;0;40m')
                    escolhavalida = False
            suasdicas = '\nSuas dicas:\n'
            if len(descolhidas[0]) > 0:
                suasdicas += descolhidas[0]
            if len(descolhidas[1]) > 0:
                suasdicas += descolhidas[1]
            if len(descolhidas[2]) > 0:
                suasdicas += descolhidas[2]
            if len(descolhidas[3]) > 0:
                suasdicas += descolhidas[3]
            if len(descolhidas[4]) > 0:
                suasdicas += descolhidas[4]
            if chances < 5:
                print(lpds+suasdicas+'\nVocê ainda tem \033[0;31;40m{}\033[0;0;40m tentativa(s)'.format(chances))
            elif chances < 10:
                print(lpds+suasdicas+'\nVocê ainda tem \033[0;35;40m{}\033[0;0;40m tentativa(s)'.format(chances))
            elif chances < 15:
                print(lpds+suasdicas+'\nVocê ainda tem \033[0;33;40m{}\033[0;0;40m tentativa(s)'.format(chances))
            elif chances <= 20:
                print(lpds+suasdicas+'\nVocê ainda tem \033[0;32;40m{}\033[0;0;40m tentativa(s)'.format(chances))

        elif palpite == 'comandos':
            print(comandos)

        elif palpite in dadosn.keys():
            if palpite.lower() == pais_sorteado:
                print('\033[1;32;40mParabéns, você acertou!!!\033[0;0;40m')
                end = True
            elif em_lpd == True:
                print('\033[0;31;40m\nNão repita palpites!\n\033[0;0;40m')
            else:
                dh = haversine(re, dadosn, pais_sorteado, palpite)
                lpd = adiciona_em_ordem(palpite, dh, lpd)
                lpds = addlpds(lpd, lpds)
                chances -= 1
                if chances < 5:
                    print(lpds+suasdicas+'\nVocê ainda tem \033[0;31;40m{}\033[0;0;40m tentativa(s)'.format(chances))
                elif chances < 10:
                    print(lpds+suasdicas+'\nVocê ainda tem \033[0;35;40m{}\033[0;0;40m tentativa(s)'.format(chances))
                elif chances < 15:
                    print(lpds+suasdicas+'\nVocê ainda tem \033[0;33;40m{}\033[0;0;40m tentativa(s)'.format(chances))
                elif chances <= 20:
                    print(lpds+suasdicas+'\nVocê ainda tem \033[0;32;40m{}\033[0;0;40m tentativa(s)'.format(chances))

        elif palpite == 'desisto':
            print('Poxa, você desistiu. O país era {}'.format(pais_sorteado))
            end = True

        else:
            print('\033[0;31;40m\nPaís desconhecido!'+' \n\033[0;0;40m')

    if chances == 0:
        print('\nSuas chances acabaram, você perdeu! O país era {}\n'. format(pais_sorteado))
        dnv = input('Deseja jogar novamente? s|n ')
        if dnv == 's':
            stop = False
        elif dnv == 'n':
            stop = True
            sair = input('\nTem certeza que quer sair do jogo? s|n ')
            if sair == 's':
                stop = True
            elif sair == 'n':
                stop = False
            else:
                print('\033[0;31;40m\nOpção inválida!\033[0;0;40m')
        else:
            print('\033[0;31;40m\nOpção inválida!\033[0;0;40m')

    elif end == True:
        sair = input('\nTem certeza que quer sair do jogo? s|n ')
        if sair == 's':
            stop = True
        elif sair == 'n':
            stop = False
        else:
            print('\033[0;31;40m\nOpção inválida!\033[0;0;40m')