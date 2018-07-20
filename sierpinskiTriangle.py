import sys

def sierpinski(n):
	toReturn = ''
	for y in range (0,n*n):
		for x in range (0,n):
			if x % n == 0:
				toReturn += '*'
		toReturn += '\n'

	return toReturn
print('1')
print('2')
print(sierpinski(int(sys.argv[1])))