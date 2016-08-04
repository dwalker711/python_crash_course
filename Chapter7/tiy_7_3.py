# 7-3 Multiples of ten

number = input("Give me a number, and I'll tell you if it's a multiple of 10! ")
number = int(number)

if number % 10 == 0:
	print("Yes! The number {} is divisible by 10!".format(number))
else:
	print("Ah, no. The number {} is NOT divisible by 10.".format(number))