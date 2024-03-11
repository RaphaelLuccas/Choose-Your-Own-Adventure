print('Bem vindo ao jogo do quiz!')

playing = input('Você quer jogar? ')

if playing.lower() != 'sim':
    print('Volte outro dia!')
    quit()

print("Muito bem! Vamos lá!")
score = 0

answer = input('O que significa a sigla CPU? ')
if answer.lower() == 'central processing unit':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')
    score 

answer = input('O que significa a sigla GPU? ')
if answer.lower() == 'graphical processing unit':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')

answer = input('O que significa a sigla RAM? ')
if answer.lower() == 'random access memory':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')

answer = input('O que significa a sigla PSU? ')
if answer.lower() == 'power supply':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')


answer = input('O que significa a sigla SPD? ')
if answer.lower() == 'serial presence detect':
    print('Correto!')
    score += 1
else:
    print('Incorreto!')


print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 5) * 100) + '%.')