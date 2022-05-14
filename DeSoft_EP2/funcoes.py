from random import choice
from math import *


# Normaliza Base de Países
def normaliza (dic):
    dicn = {}
    for k, v in dic.items():
        for k2, v2 in v.items():
            dicn[k2] = v2
            v2['continente'] = k
    return dicn


# Sorteia Países
def sorteia_pais (dic):
    return choice(list(dic))



# Calcula Distância de Haversine
def haversine (r, dic, pais1, pais2):
    
    for k, v in dic.items():
        if k == pais1:
            phi1 = radians(v['geo']['latitude'])
            lambda1 = radians(v['geo']['longitude'])
        elif k == pais2:
            phi2 = radians(v['geo']['latitude'])
            lambda2 = radians(v['geo']['longitude'])
    
    termo1 = sin((phi2-phi1)/2)**2
    termo2 = cos(phi1) * cos(phi2) * sin((lambda2-lambda1)/2)**2
    d = 2*r * asin((termo1 + termo2)**(1/2))
    return d
            


# Adiciona em uma Lista Ordenada
def adiciona_em_ordem (nome_pais, dist, lpd):
    if lpd == []:
        lpd.append([nome_pais, dist])
    else:
        for i in range(0, len(lpd)):
            if lpd[i][1] > dist:
                lpd.insert(i, [nome_pais, dist])
                break
            elif i == len(lpd)-1:
                lpd.append([nome_pais, dist])
    return lpd


# Checa presença na lista
def esta_na_lista (nome_pais, lpd):
    presente = False
    for l in lpd:
        if l[0] == nome_pais.lower():
            presente = True
            break
    return presente


# Sorteia Letra com Restrições
def sorteia_letra (palavra, lista_restricao):
    
    validos = []
    caract_esp = ['.', ',', '-', ';', ' ']
    
    for caract in palavra.lower():
        if caract not in lista_restricao and caract not in caract_esp:
            validos.append(caract)
    
    if validos == []:
        return ''
    else:
        return choice(validos)


# Distância entre países (lista --> string)
def addlpds (lpd, lpds):
    lpds = ''
    lpds = '\nDistâncias: \n'
    for i in range(0, len(lpd)):
        if lpd[i][1] < 600:
            lpds += '\033[1;32;40m{} km --> {} \n'.format(lpd[i][1], lpd[i][0])
        elif lpd[i][1] < 1600:
            lpds += '\033[1;33;40m{} km --> {} \n'.format(lpd[i][1], lpd[i][0])
        elif lpd[i][1] < 4000:
            lpds += '\033[1;35;40m{} km --> {} \n'.format(lpd[i][1], lpd[i][0])
        elif lpd[i][1] < 10000:
            lpds += '\033[1;31;40m{} km --> {} \n'.format(lpd[i][1], lpd[i][0])
        else:
            lpds += '\033[1;30;40m{} km --> {} \n'.format(lpd[i][1], lpd[i][0])
    lpds += '\033[0;0;40m\n'
    return lpds

