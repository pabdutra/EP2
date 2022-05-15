# Introdução:
intro = '\033[0;34;40m='*34+'\n|                                |\n|   \033[1;37;40mBem-vindo ao Insper Países   \033[0;34;40m|\n|                                |\n\033[0;34;40m======= \033[0;36;40mDesign de Software \033[0;34;40m=======\n'
chamada = '\n\033[0;34;40mUm país foi escolhido, tente adivinhar!\n\033[0;34;40m'
comandos = '\033[3;37;40m\nComandos:\n    Dica       - Entra no mercado de dicas\n    Desisto    - Desiste da rodada\n    Comandos   - Mostra novamente os comandos disponíveis\n\033[0;0;40m'


# Dicas
dicaspadrao = '------------------------------------------\n            Mercado de dicas\nLegenda: {}\033[0;0;40m ; {} \033[3;37;40m\nDigite 0 para retornar aos palpites\n------------------------------------------\n\033[0;0;40m'.format('\033[0;34;40mNumero da dica', '\033[0;36;40mCusto da dica')

dica1 = '\033[0;34;40m1 \033[0;0;40m- Letra da capital (\033[0;36;40m3 tentativas\033[0;0;40m)\n'
dica2 = '\033[0;34;40m2 \033[0;0;40m- Cor da bandeira (\033[0;36;40m4 tentativas\033[0;0;40m)\n'
dica3 = '\033[0;34;40m3 \033[0;0;40m- População (\033[0;36;40m5 tentativas\033[0;0;40m)\n'
dica4 = '\033[0;34;40m4 \033[0;0;40m- Área (\033[0;36;40m6 tentativas\033[0;0;40m)\n'
dica5 = '\033[0;34;40m5 \033[0;0;40m- Continente (\033[0;36;40m7 tentativas\033[0;0;40m)\n'

letras_compradas = []
lddisponiveis = [dica1, dica2, dica3, dica4, dica5]


descolhidas = ['', '', '', '', '']

suasdicas = 'Suas dicas:\n'
            