from time import sleep
from random import randint
from colorama import Fore,Style

shown_text= " Happy Holiday Github.com "
my_base=len(text1)
my_base += 1

while True:
	print('\033c')
  
	for x in range(1, my_base, 2):
		y = randint(2, 12)
		if x==1:
			print(f"{Style.BRIGHT}{Fore.YELLOW}{'\u2721':^40}")
      
		elif y%5==0:
				print(f"{Fore.RED}{shown_text[:x]:^40}")
        
		elif y%3==0:
				print(f"{Fore.GREEN}{shown_text[:x]:^40}")
        
		else:
			print(f"{Fore.WHITE}{shown_text[:x]:^40}")
      
	print(f"{Fore.WHITE}{'||||':^39}")
	print(f"{Fore.WHITE}{'||||\n':^39}")
	print(f"{Fore.WHITE}{'Github.com/signorrayan':^39}")
	sleep(.50)
