#
#	Problem Statement: https://www.codechef.com/problems/BLONDIE
#
#	Video Link: 
#
#	Instagram: http://instagram.com/aakashverma1102
#	LinkedIn: https://www.linkedin.com/in/aakashverma1124/
#

def solve(arr, n):
	prefix_sum = 0
	ans = []
	for i in range(0, n):
		if arr[i] != -1:
			ans.append(arr[i])
		else:
			ans.append(prefix_sum//i)
		prefix_sum += ans[i]

	return ans


if __name__ == '__main__':
	
	test = int(input())
	while test > 0:
		n = int(input())
		arr = list(map(int, input().split()))
		ans = solve(arr, n)
		for i in ans:
			print(i, end = " ")
		print()
		test -= 1