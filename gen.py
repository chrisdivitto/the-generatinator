#!/usr/bin/python3

import random


gender=random.randint(0,1)
if gender ==0:
	gender = ("male")
if gender ==1:
	gender = ("female")

race=random.randint(0,4)
if race ==0:
	race = (' human')
if race ==1:
	race = (' elf')
if race ==2:
	race = (' gnome')
if race ==3:
	race = (' dwarf')
if race ==4:
	race = (' half elf')

character=gender+race

userchoice = input('input: ')

if userchoice == 'npc':
	print (character + '\n \n \n \n')
