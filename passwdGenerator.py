import string
import random


# criando a lista de caracteres para gerar a senha
characters = list('+!@#$%&*()-_?^ç.[]' + string.ascii_letters + string.digits)

def randomPasswordGenerator():
    length = int(input('Informe a quantidade de caracteres da senha: '))

    #random.shuffle(characters)

    password = []

    for i in range(length):
        password.append(random.choice(characters))


    random.shuffle(password)

    print(''.join(password))


randomPasswordGenerator()
