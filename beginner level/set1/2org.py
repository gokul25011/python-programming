n=raw_input()
if n.isdigit():
	a=int(n)
	if(a%2==0):
		print("Even")
	else:
		print("Odd")
else:
	print("invalid input")
