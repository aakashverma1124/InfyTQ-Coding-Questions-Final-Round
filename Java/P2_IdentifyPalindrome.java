/*
*	Problem Statement:
*	For a given positive number num, identify the palindrome formed by performing the following operations-
*	1. Add num and its reverse 
*	2. Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a palindrome is obtained 
*	
*	Video Link: 
*
*	Instagram: http://instagram.com/aakashverma1102
*	LinkedIn: https://www.linkedin.com/in/aakashverma1124/
*
*/

import java.util.*;

class IdentifyPalindrome {

	public static int reverse(int num) {
		StringBuilder string = new StringBuilder(Integer.toString(num));
		string.reverse();
		return Integer.parseInt(string.toString());
	}

	public static boolean isPalindrome(int num) {
		return num == reverse(num);
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		while(true) {
			num = num + reverse(num);
			if(isPalindrome(num)) {
				System.out.println(num);
				break;
			}
		}
		
	}
}

