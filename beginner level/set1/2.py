n=raw_input()
if n.isdigit():
	a=int(n)
	if(a%2==0):
		print("even")
	else:
		print("odd")
else:
	print("invalid input")
