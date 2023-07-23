n = int(input("Enter length of Fibonacci series: "))
num1 = 0
num2 = 1
nextnumber = 0
count = 1

while(count <= n):
	print(nextnumber, end=" ")
	count += 1
	num1 = num2
	num2 = nextnumber
	next20number = num1 + num2
	t_number = num1 + num2
