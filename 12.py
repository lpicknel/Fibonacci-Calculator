a = 0
b = 1 
for x in range(1,26):
	if(x == 1):
		print (str(x) + ":1")
	else:
		c = a + b 
		print(str(x) + ":" + str(c))
		a = b
		b = c