f = open("file", "r")
digits = []
for line in f:
	first = -1
	last = -1
	for c in line:
		if c.isdigit():
			if first == -1:
				first = int(c)
			last = int(c)
	digits.append(first * 10 + last)
f.close()
sum = 0
for d in digits:
	sum += d
print(sum)
