n=raw_input()
if n.isdigit():
	a=int(n)
	if(a<0):
		print("Negative")
	elif(a==0):
		print("Zero")
	else:
		print("Positive")
else:
	print "invalid"
