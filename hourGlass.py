#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

arr = [
	[-1,1,-1,0,0,0],
	[0,-1,0,0,0,0],
	[-1,-1,-1,0,0,0],
	[0,-9,2,-4,-4,0],
	[-7,0,0,-2,0,0],
	[0,0,-1,-2,-4,0]
]


currentMax = None
temp = 0

counter = 0

for x in range (0, 4):
	for y in range(0, 4):
			temp = 0
			temp += arr[y][x] + arr[y][x + 1] + arr[y][x + 2]
			temp += arr[y+1][x + 1]
			temp += arr[y+2][x] + arr[y+2][x + 1] + arr[y+2][x + 2]

			if currentMax is None or currentMax < temp:
				currentMax = temp

			counter += 1
			print(counter, temp)



print(currentMax)

