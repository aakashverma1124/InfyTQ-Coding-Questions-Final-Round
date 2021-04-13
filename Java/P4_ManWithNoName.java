/*
*	Problem Link: https://www.codechef.com/problems/BLONDIE
*
*	Video Link: 
*
*	Instagram: http://instagram.com/aakashverma1102
*	LinkedIn: https://www.linkedin.com/in/aakashverma1124/
*
*/

import java.util.*;
import java.io.*;

class ManWithNoName {
    
    public static long[] solve(long arr[], int n) {
        long ans[] = new long[n];
        long prefixSum = 0;
        for(int i = 0; i < n; i++) {
            if(arr[i] != -1) {
                ans[i] = arr[i];
            }
            else {
                ans[i] = prefixSum/(i);
            }
            prefixSum += ans[i];
        }
        return ans;
    }
    
	public static void main (String[] args) throws java.lang.Exception {
		Scanner scan = new Scanner(System.in);
		int test = scan.nextInt();
		while(test-->0) {
		    int n = scan.nextInt();
		    long arr[] = new long[n];
		    for(int i = 0; i < n; i++) {
		        arr[i] = scan.nextLong();
		    }
		    long ans[] = solve(arr, n);
		    for(int i = 0; i < n; i++) {
		        System.out.print(ans[i] + " ");
		    }
		    System.out.println();
		}
	}
}