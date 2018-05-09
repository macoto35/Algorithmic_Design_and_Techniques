package algo;

import java.io.*;
import java.util.*;

public class NumInversion {

	static int sum = 0;
	
	private static int[] merge(int[] A, int[] B) {
		int[] C = new int[A.length + B.length];
		int aIdx = 0;
		int bIdx = 0;
		int cIdx = 0;
		
		while(A.length > aIdx && B.length > bIdx) {
			int a = A[aIdx];
			int b = B[bIdx];
			
			if (a <= b) {
				C[cIdx++] = a;
				aIdx++;
			} else {
				C[cIdx++] = b;
				bIdx++;
				
				sum += A.length - aIdx;
			}
		}
		
		for(int i = aIdx ; i < A.length ; i++)
			C[cIdx++] = A[i];

		for(int i = bIdx ; i < B.length ; i++)
			C[cIdx++] = B[i];
		
		return C;
	}
	
	private static int[] numOfInversion(int[] arr, int st, int ed) {
		if (st == ed)
			return new int[]{ arr[st] };
		
		int m = st + (int) Math.floor((ed - st) / 2);
		
		int[] A = numOfInversion(arr, st, m);
		int[] B = numOfInversion(arr, m+1, ed);
		
		return merge(A, B);
	}
	
	public static void main(String[] args) {
		try {
			//Scanner scanner = new Scanner(System.in);
			Scanner scanner = new Scanner(new FileInputStream("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/4_4_inversions.in"));
			
			int n = scanner.nextInt();
			int[] arr = new int[n];
			for (int i = 0 ; i < n ; i++)
				arr[i] = scanner.nextInt();
			
			for (int i : numOfInversion(arr, 0, n - 1)) {
				System.out.print(i + " ");
			}
			System.out.println();
			System.out.println(sum);
			
			scanner.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}
