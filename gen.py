#!/usr/bin/python3

# Hello! Welcome to this program!
# If you are a seasoned programmer that has somehow found your way to this project,
# it'd probably take you 2 seconds to realize I have no idea what I am doing.
# This is correct. My code is awful, but as of now, it works.
# This tool is made specifically for my use, but maybe it could help you too
# Enjoy!

import random
userchoice = ' '

# Handling inputs
while userchoice != 'exit':
	userchoice = input('input: ')

	if userchoice == 'npc':
		# NPC Generation
		age=random.randint(0,3)
		if age ==0:
			age = ('child ')
		if age ==1:
			age = ('young ')
		if age ==2:
			age = ('middle aged ')
		if age ==3:
			age = ('elderly ')

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

		quality=random.randint(0,3)
		if quality ==0:
			quality = (', they are kind')
		if quality ==1:
			quality = (', they are mean.')
		if quality ==2:
			quality = (', they are indifferent about you, and don\'t seem particularly interested in their surroundings.')
		if quality ==3:
			quality = (', they are grumpy.')

		print ('\n' + '\x1b[32m' + age + gender + race + quality + '\x1b[0m' + '\n')

	if userchoice == 'dungeon':
		# Dungeon Generation
		dungeontype=random.randint(0,8)
		if dungeontype ==0:
			dungeontype = ('an abandoned castle')
		if dungeontype ==1:
			dungeontype = ('a cult hideout')
		if dungeontype ==2:
			dungeontype = ('a mysterious cave')
		if dungeontype ==3:
			dungeontype = ('a large hallowed out tree')
		if dungeontype ==4:
			dungeontype = ('a haunted house')
		if dungeontype ==5:
			dungeontype = ('a volcanic cavern')
		if dungeontype ==6:
			dungeontype = ('a temple to an old god')
		if dungeontype ==7:
			dungeontype = ('a complex sewer system')
		if dungeontype ==8:
			dungeontype = ('a heavily gaurded prison')

		location=random.randint(0,5)
		if location ==0:
			location = (' just outside of town.')
		if location ==1:
			location = (' past the nearby river.')
		if location ==2:
			location = (' on the highest mountain in the region.')
		if location ==3:
			location = (' hidden in the forest.')
		if location ==4:
			location = (' hidden underground beneath the tavern.')
		if location ==5:
			location = (' submerged at the bottom of the nearby lake.')

		print ('\n' + '\x1b[32m' + dungeontype + location + '\x1b[0m' + '\n')


	if userchoice == 'town name':
		# Town Name Generation
		firstparttn = ["hill","east","west","north","south","illi","dark","cahh","water","river","lane","ac","aire","perl","ark","wim","black","red","bridge","lake","zon","willow","bran"]
		pickfirsttn=random.choice(firstparttn)
		secondparttn = ["march","wood"," forest","reach","far","fen","mear","rush","run","dale","cost","shaw","gon","gorn","gow","borne","ton","ben","view","don","morden","ania","vaara"," point"]
		picksecondtn=random.choice (secondparttn)
		print ('\n' + '\x1b[32m' + pickfirsttn + picksecondtn + '\x1b[0m' + '\n')


	if userchoice == 'god':
		gender=random.randint(0,1)
		if gender ==0:
			malegodname = ["elio","leon","ardo","galdo","aego","drago","fion","seca","cino","efdos","proth","gob","borr","tor","brott","morse","quaar","acullo","baartho","taa'elo","morthos","gurd","daf"]
			godname=random.choice(malegodname)
			godtitle = (' god of ')

		if gender ==1:
			femalegodname = ["elia","leona","aar'ya","galla","draca","kina","oaras","tilema","akeran","iwlena","ophelia","am'sa","fiera","feon'a","baara","kata","rina","phila","azela","a'lia","darna","amis","athys"]
			godname=random.choice(femalegodname)
			godtitle = (' goddess of ')

		element = ["thunder","fire","dreams","miracles","order","strength","harvest","war","chaos","magica","pleasure","love","ice","prosperity","health","wind","the sea","air","nature","envy","luck","secrets","the afterlife","light"]
		godelement=random.choice(element)

		print ('\n' + '\x1b[32m' + godname + godtitle + godelement + '\x1b[0m' + '\n')

	if userchoice == 'exit':
		print ('\n' + '\x1b[32m' + 'thank you, goodbye :)' + '\x1b[0m' + '\n')
