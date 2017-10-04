import re

hand = open("regex_sum_31732.txt") 
sumlist = []
for line in hand:
	line = line.rstrip()
	y = re.findall('[0-9]+', line)
	for num in y:
		sumlist.append(int(num))
print(sum(sumlist))
