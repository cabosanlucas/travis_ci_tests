import os

print("hi")
with open('feedback.txt', 'w') as f:
	f.write(os.getcwd())
