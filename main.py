print()
print('Olá, esse quiz foi feito para aprimorar minhas habilidades em iterar dicionários no Python. ')

def ready_game():
    print()
    ready = input('Você está pronto para começar o quiz? [S]ão ou [N]ão: ')

    if not ready == 's':
        print()
        print('Que pena! Eu espero você ficar pronto! :)')
        return ready_game()

    elif ready == 's':
        print()
        print('Vamos lá! ')
        pass

print()
ready_game()

perguntas = {
    'Questao 1' : {
        'pergunta' : 'De onde é a invenção do chuveiro elétrico? ',
        'resposta' : {
            'a)' : 'França',
            'b)' : 'Inglaterra',
            'c)' : 'Brasil',
            'd)' : 'Austrália',
            'e)' : 'Itália'},
            'resposta_certa' : 'c',
        },
    'Questao 2': {
        'pergunta': 'Quantas casas decimais tem o número pi? ',
        'resposta': {
            'a)': 'Duas',
            'b)': 'Centenas',
            'c)': 'Infinitas',
            'd)': 'Vinte',
            'e)': 'Milhares'},
            'resposta_certa': 'c'
        }
    }

respostas_certas = 0

for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['resposta'].items():
        print(rk, rv)

    resposta_usuario = input('Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('UHUUUL ! Resposta correta :)')
        print()
        respostas_certas += 1
    else:
        print('Que pena ! Você errou :(')
        print()

total_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / total_perguntas * 100

print(f'---------- FIM DO JOGO ----------!\n'
      f'Você teve uma porcentagem de acertos de {porcentagem_acerto}%')




