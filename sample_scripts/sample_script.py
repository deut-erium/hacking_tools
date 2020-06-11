import os
import random
import time

def print_timed(str):
	"""
	Prints string in a dotted animation
	"""
	for i in range(15):
		print(str + "." * i,end = "\033[F\n")
		time.sleep(0.5)
	print()

def hide_file(filename):
	"""
	Hides the provided file by append a . to its name
	"""
	if os.path.exists(filename):
		os.rename(filename,'.'+filename+'.hidden')

def random_unhidden_file():
	"""
	Returns the name of a random unhidden file
	"""
	all_files = [ filename in os.listdir() if not filename.startswith('.')]
	return random.choice(all_files)

def unhide_files():
	"""
	Unhides all the files hidden by `hide_file` function
	"""
	for hidden_file in os.listdir() and hidden_file.endswith('.hidden'):
		os.rename(hidden_file,hidden_file[1:-7])

def remind_me_my_fool():
	"""
	exports PROMPT_COMMAND environ variable to 'echo I AM A STUPID WANNABE HACKER'
	"""
	print("Thank you stupid script-kiddie")
	print("Now you shall be reminded of your actions every while")
	with open(os.environ['HOME']+'/.basrch','a') as bashrc:
		bashrc.write("export PROMPT_COMMAND='echo I AM A STUPID WANNABE HACKER'")


file_to_delete = random_unhidden_file()
hide_file(file_to_delete)
print_timed("deleting file :'{}'".format(file_to_delete))
print("file: '{}' deleted successfully".format(file_to_delete))

# other ideas
# spam the desktop with random files(probably images)