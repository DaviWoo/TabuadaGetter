from random import randint
from termcolor import colored
from datetime import datetime
from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('minisound.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# Prints iniciais
#print('\n'*30) APRESENTATIVO
print(colored('TABUADA GETTER\n', 'red'))
#sleep(2.5) APRESENTATIVO
print('Este programa lhe ajudará a estudar a tabuada. Você responderá multiplicações\n'
      'aleatórias de acordo com a tabuada dos números que decidir estudar.')
print(colored('Aguardando...', 'magenta'))
cn = str(input('\nDigite algo para continuar: ' + '\n'*7))
print('\n'*30)
# -----------------------------------------------------------------------------

# Declaração das listas, variáveis, e o laço para criar a tabuada
nums = list()
results = list()
erros = list()
erros_results = list()
tempos = list()
resps = list()

print(colored('De qual até qual número da tabuada deseja estudar?: ', 'cyan'))
first = int(input('Primeiro número: '))
second = int(input('Último número: '))

for c in range(first, second + 1):
    for p in range(1, 11):
        nums.append([c, p])
        results.append([c * p])
# ----------------------------------------------

print('As perguntas começarão em 4 segundos...\nDigite "S" de "SAIR" para parar')
sleep(5)
cont = 0

# Laço onde se fazem as perguntas de tabuada
while True:
    escolha = randint(0, len(nums)-1)
    tic = datetime.now()
    rsp = str(input(f'{nums[escolha][0]} x {nums[escolha][1]} resulta em: '))

    if rsp in 'SsSairSAIR' and cont != 0: break
    while rsp in 'SsSairSAIR' and cont == 0:
        print(colored('Responda ao menos uma pergunta para sair', 'red'))
        escolha = randint(0, len(nums))
        sleep(2)
        tic = datetime.now()
        rsp = str(input(f'{nums[escolha][0]} x {nums[escolha][1]} resulta em: '))
        toc = datetime.now() - tic

    resp = int(rsp)
    toc = datetime.now() - tic


    if resp == results[escolha][0]:
        print(colored('Você ACERTOU!\n', 'yellow'))


    elif resp != results[escolha][0]:
        print(colored('Você ERROU!\n', 'red'))
        erros.append([nums[escolha][0], nums[escolha][1]])
        erros_results.append(results[escolha][0])
        print(colored(f'A resposta correta era {results[escolha][0]}', 'red'))
        sleep(2)

    tictoc = f'{toc}'
    tac = f'{tictoc[5]}{tictoc[6]}{tictoc[7]}{tictoc[8]}'
    tac_int = float(tac)
    resps.append([nums[escolha][0], nums[escolha][1]])
    tempos.append(tac_int)
    cont += 1
    print(f'Você demorou {tac_int} segundos para responder')
    sleep(2)
# ---------------------------------------------------------------------------------------------

print('\nEste foi o seu tempo para responder a cada pergunta: ')

# Laço que coloca os tempos coloridos
cyan = 0
yellow = 0
green = 0
red = 0

for c in range(0, len(tempos)):
    print(f'{resps[c][0]} x {resps[c][1]}: ', end='')
    if tempos[c] <= 2.0:
        print(colored(f'{tempos[c]}s', 'cyan'))
        cyan += 1
    elif tempos[c] > 2.0 and tempos[c]<= 2.5:
        print(colored(f'{tempos[c]}s', 'yellow'))
        yellow += 1
    elif tempos[c]> 2.5 and tempos[c] <= 3.2:
        print(colored(f'{tempos[c]}s', 'green'))
        green += 1
    elif tempos[c] > 3.2:
        print(colored(f'{tempos[c]}s', 'red'))
        red += 1
# ---------------------------------------------------------------------------------------

print(colored('\nVermelho: HORRÍVEL', 'red'))
print(colored('Verde: Mais ou menos', 'green'))
print(colored('Amarelo: Ótimo', 'yellow'))
print(colored('Ciano: MESTRE', 'cyan'))

print(f'Você obteve {cyan} cianos. Parabéns!')
print(f'Você obteve {yellow} amarelos. Está bonzinho...')
print(f'Você obteve {green} verdes. Treine mais')
print(f'Você obteve {red} vermelhos. Treine mais')
print(f'\nSua média de tempo é de {sum(tempos) / len(tempos):.2f}s')

cn = str(input('Digite algo para continuar: '))

if len(erros) > 0:
    print('\n'*30)
    print(colored('Hora de revisar seus erros', 'cyan'))
    print(colored(f'Você tem {len(erros)} ERRO(S) para revisar', 'red'))
    print('3...2...1...\n')
    sleep(4)

while len(erros) != 0:
    for c in range(0, len(erros)):
        tic = datetime.now()
        resp = int(input(f'{erros[c-1][0]} x {erros[c-1][1]} resulta em: '))

        toc = datetime.now() - tic
        tictoc = f'{toc}'
        tac = f'{tictoc[5]}{tictoc[6]}{tictoc[7]}{tictoc[8]}'
        tac_int = float(tac)

        if resp == erros_results[c]:
            print(colored('Você ACERTOU! Erro revisado', 'cyan'))
            print(f'Você demorou {tac_int} segundos para responder')
            sleep(4)
            del erros[c]

        else:
            print(colored('Você ERROU! Precisa revisar mais', 'red'))
            print(f'Você demorou {tac_int} segundos para responder')
            sleep(4.5)

print('\nPrograma encerrado. Volte sempre')