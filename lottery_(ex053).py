#exercício88
print('='*45)
print('{:-^45}'.format('< JOGOS DA MEGA SENA >'))
print('='*45)
amount = int(input('Quantos jogos você quer que eu sorteie? '))
print('='*45)
print('{:-^45}'.format('< SORTEANDO {} JOGOS >'.format(amount)))
print('='*45)
for play in range(0, amount):
    amount_numbers = 0
    mega_sena = []
    while True:
        number = randint(1, 61)
        if number not in mega_sena:
            mega_sena.append(number)
            amount_numbers += 1
        if amount_numbers > 6:
            break
    sleep(1)
    print(f'{play+1}º Jogo: ', end='')
    print(sorted(mega_sena))
sleep(1)
print('='*45)
print('{:-^45}'.format('< BOA SORTE! >'))
print('='*45)