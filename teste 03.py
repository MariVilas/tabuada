import random
from time import sleep

def tabuada(x):
    for cont in range(1,11):
        print('{0} x {1} = {2}'.format(x,cont,x*cont))

if __name__=='__main__':
    print('-' * 40)
    print(f'{"Calculando a tabuada:"}')
    print('-' * 40)

    num = int(input('Digite um número: '))
    print("Cal\n")
    sleep(1)
    print("cu\n")
    sleep(1)
    print("lando!!!\n")
    tabuada(num)

