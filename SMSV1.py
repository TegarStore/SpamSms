import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
\033[1;35m____  ____   _    __  __    ____  __  __ ____
/ ___||  _ \ / \  |  \/  |  / ___||  \/  / ___|
\___ \| |_) / _ \ | |\/| |  \___ \| |\/| \___ \
 ___) |  __/ ___ \| |  | |   ___) | |  | |___) |
|____/|_| /_/   \_\_|  |_|  |____/|_|  |_|____/
--------------------------------------
\033[1;32mAUTHOR  \033[1;31m :\033[1;0m TEGAR STORE
\033[1;32mWHATSAPP \033[1;31m : \033[1;0m 085893093052
--------------------------------------
1. SMS Gratis
2. OTP Hallodok
\033[1;31m𝗦𝗔𝗕𝗔𝗥 𝗣𝗜𝗟𝗜𝗛 𝗡𝗬𝗔 𝗞𝗔𝗞 🥺
""")
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.alodok
	
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))