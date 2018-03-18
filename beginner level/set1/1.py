a=raw_input()
if a.isdigit():
	if(a<0):
		print("negative")
	elif(a>0):
		print("positive")
	else:
		print("zero")
else:
	print("invalid input")
