/*
*	Problem Statement:
*	The input is a N x N matrix where some of the items in the matrix are 0.
*	If any of the items are 0, then set that item's entire row and column to 0.
*	items that are not 0 will be represented by an integer.
*
*	Video Link: https://youtu.be/YgguFLwBwIE
*
*	Instagram: http://instagram.com/aakashverma1102
*	LinkedIn: https://www.linkedin.com/in/aakashverma1124/
*
*/

import java.util.*;

class ZeroMatrix {

	public static int[][] setZero(int matrix[][], int n) {
		boolean zeroRows[] = new boolean[n];
		boolean zeroCols[] = new boolean[n];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(matrix[i][j] == 0) {
					zeroRows[i] = true;
					zeroCols[j] = true;
				}
			}
		}

		for(int i = 0; i < n; i++) {
			if(zeroRows[i]) {
				for(int col = 0; col < n; col++) {
					matrix[i][col] = 0;
				}
			}
		}

		for(int i = 0; i < n; i++) {
			if(zeroCols[i]) {
				for(int row = 0; row < n; row++) {
					matrix[row][i] = 0;
				}
			}
		}
		return matrix;

	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[][] arr = new int[n][n];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				arr[i][j] = scan.nextInt();
			}
		}
		int ans[][] = setZero(arr, n);
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.print(ans[i][j] + " ");
			}
			System.out.println();
		}
	}
}

