#
#   Problem Statement:
#   Consider an array inarr containing atleast two&nbsp;non-zero positive integers ranging between 1 to 300
#   (inclusive of the boundary values). Divide the integers in inarr into two groups based on the below rules:
#   1. Each of the integers should belong to either of the two groups.
#   2. The total sum of integers in each of the groups must be as nearly equal as possible.
#   3. The total number of integers between the two groups should not differ by more than 1.
#   Print outnum1 and outnum2, the sum of the integers of two groups separated by a space.
#   If outnum1 and outnum2 are not equal, then print the smallar sum followed by the larger sum.
#
#   Example: 
#   Input: 87,100,28,67,68,41,67,1
#   Output: 229 230
#   
#   Video Link: https://youtu.be/G_owQ4_OH4w
#
#   Instagram: http://instagram.com/aakashverma1102
#   LinkedIn: https://www.linkedin.com/in/aakashverma1124/
#
#

def solve(arr, last_index, S1, S2, lenS1, lenS2):
        
    if(last_index < 0):
        if(abs(lenS1 - lenS2) > 1):
            return 10**9
        return abs(S1 - S2)
    return min(solve(arr, last_index - 1, S1, S2, lenS1, lenS2), 
                            solve(arr, last_index - 1, S1 + arr[last_index], S2 - arr[last_index], lenS1 + 1, lenS2 - 1))
    

if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    n = len(arr)
    total_sum = sum(arr)
    min_diff = solve(arr, n - 1, 0, total_sum, 0, n)
    print(int(total_sum/2 - min_diff/2), int(total_sum/2 + min_diff/2))


