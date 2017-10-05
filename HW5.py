
import re

file = input('Enter file name: ')

fopen = open(file)

lst = []
sum = 0
for line in fopen:
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	lst.extend(num)

for item in lst:
	sum += int(item)

print(sum)
