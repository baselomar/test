
import os

os.system("clear")
os.system("cd && cd test")
os.system("bash TOOL.sh")
print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Normal login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Tokens login"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	login_method = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if login_method =="":
		print"\033[1;91m[!] Wrong input"
		exit()
	elif login_method =="1":
		login()
	elif login_method =="2":
		fbtoken()
	elif login_method =="0":
		exit()
	else:
		print"\033[1;91m[!] Wrong input"
		exit()

