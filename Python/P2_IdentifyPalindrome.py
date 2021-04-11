#
#	Problem Statement:
#	For a given positive number num, identify the palindrome formed by performing the following operations-
#	1. Add num and its reverse 
#	2. Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a palindrome is obtained 
#	
#	Video Link: 
#
#	Instagram: http://instagram.com/aakashverma1102
#	LinkedIn: https://www.linkedin.com/in/aakashverma1124/
#

def reverse(num):
	return int(str(num)[::-1])

def is_palindrome(num):
	return num == reverse(num)

if __name__ == '__main__':
	num = int(input())
	while True:
		num = num + reverse(num)
		if(is_palindrome(num)):
			print(num)
			break