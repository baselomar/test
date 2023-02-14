
import os

os.system("clear")
os.system("cd && cd test")
os.system("bash TOOL.sh")

print "║login"
	print "║Tokens login"
	print "║ Exit"
	print "\033[1;97m║"
	login_method = raw_input("╚═>>>")
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

