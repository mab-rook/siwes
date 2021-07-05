#return the first element in a list

# creating an empty list
lst = []

# number of elements as input
first = []

n = int(input("Enter numbers : "))

for i in range(0, n):
	element = int(input())

	first.append(element) 

print(first)
print(first[0])

