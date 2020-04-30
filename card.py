import time
import random
card_turple=('Spiderman','Ironman','Loki','Thor','Cap')
package={}
weight=(5,10,50,50,100)
compare=(15,35,115,215)
while 1:	
	choice=int(input('1.draw a card\n 2.look into the bag\n 3.leave.\n Which number do you choose?'))

	if choice ==1:
		num =int(input('how many times?'))
		for i in range(0,num):
			n= random.randint(1,weight[-1])
			i=0
			while n>compare[i]:
				i=i+1
			print('you got{}'.format(card_turple[i]))
			if package.__contains__(card_turple[i]):
				package[card_turple[i]] +=1
			else:
				package[card_turple[i]] =1	
			print('put {} in in the bag already'.format(card_turple[i]))
			print('--------------------') 
			time.sleep(0.3)		
	if choice ==2:
		if  len(package)==0:
			print('nothing here')
			print('--------------------')
			
		else:
			for key,value in package.items():
				print('{}, number{}'.format(key,value))
				print('--------------------')
	if choice==3:
		break
