import os,time,sys
from os import system

def slow(n):
	for word in n + "\n":
		sys.stdout.write(word)
		sys.stdout.flush()
		time.sleep(0.03)
def fast(n):
	for word in n + "\n":
		sys.stdout.write(word)
		sys.stdout.flush()
		time.sleep(0.01)
def ml():
	try:
		os.system("rm -rf /sdcard/Android/data/com.mobile.legends/cache/*")
		slow(berhasil)
	except: pass
def ff():
	try:
		os.system("rm -rf /sdcard/Android/data/com.dts.freefireth/cache/*")
		slow(berhasil)
	except: pass
def all():
	try:
		ml()
		ff()
	except: pass

banner="""
 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""
menu="""
(+) MENU (+)

	(1) SAMPAH MOBILE LEGENDS
	(2) SAMPAH FREE FIRE
	(3) SAMPAH ML & FF
	(4) EXIT
"""
berhasil="(+) BERHASIL MENJALANKAN CLEANER (+)"
os.system("clear")
fast(banner)
slow(menu)
slow("(+) PILIH (+)")
los=input("(+) > ")
def home():
	print ("")
	if los == "1":
		ml()
		print ("")
	elif los == "2":
		ff()
		print ("")
	elif los == "3":
		all()
		print ("")
	elif los == "4":
		slow("(+) EXIT THE TOOLS (+)")
		slow("(+) BYE BYE (+)")
		os.system("exit")
	else:
		slow("(+) ERROR YOUR CHOSE NOT IN MENU (+)")
		os.system("exit")

if __name__ == "__main__":
	home()
