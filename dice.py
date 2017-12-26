#!/usr/bin/python3

import random
dicechoice = ' '

while dicechoice != 'exit':

    dicechoice = input('dice: d')
    changer = input('plus: ')
    if changer == (''):
        changer = ('0')

    result=random.randint(1,int(dicechoice))
    if int(dicechoice) ==20:
        if result ==1:
            final = ('critical fail')
        if result ==20:
            final = ('nat 20')
        else:

            final = int(result) + int(changer)

    else:
        final = int(result) + int(changer)

    print ('\n' + '\x1b[32m' + str(final) + '\x1b[0m' + '\n')

    if dicechoice == 'exit':
            print ('thank you goodbye')
