def strxor(a,b):
	if a==b:
		return '0'
	return '1'


def check(x,y):
	pos = 0
	while pos + len(y) < len(x) and '1' in x:

		for i in range(len(y)):
			x[pos+i] = strxor(x[pos+i],y[i])

		while x[pos]!='1' and '1' in x:
			pos+=1

	if '1' in x:
		return False
	return True


x = list(input())

y = list(input())

if check(x,y):
	print("no errors")
else:
	print("errors")