import os
print(os.getcwd())
with open("new_file.txt", w) as f:
	f.write(os.getcwd())

