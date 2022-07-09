print("\033[1;36;40mOlá Mundo\033[m")
print("\033[35mHello World! ")
print("\033[4;31;40mOlá Mundo! ")
print("\033[7;30;43mHello World!\033[m ")

nome = 'Eduardo'
cores = {'limpa':'\033[m',
         'azul':'\033[m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print("Olá! Muito prazer em te conheçer{},{},{}!!".format(cores['azul'], nome , cores['limpa']))