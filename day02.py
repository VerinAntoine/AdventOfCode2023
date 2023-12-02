
def is_valid_count(n: int, color: str):
	if color == "red" and n <= 12:
		return True
	if color == "green" and n <= 13:
		return True
	if color == "blue" and n <= 14:
		return True
	return False

f = open("file", "r")
valids = []
game = 0
for line in f:
	line = line.strip("\n")		# Removing \n char for each line
	line = line.split(": ")[1]	# Removing useless "Game X:"
	draw = line.split("; ")
	valid = 1
	game += 1
	for cubes in draw:
		cubes = cubes.split(", ")
		for cube in cubes:
			cube = cube.split(" ")
			n = int(cube[0])
			color = cube[1]
			if not is_valid_count(n, color):
				valid = 0
	if valid == 1:
		valids.append(game)
sum = 0
for game in valids:
	sum += game
print(sum)
