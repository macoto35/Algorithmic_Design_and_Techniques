package algo;

import java.util.*;

public class MaxNumPrice {

	private static int naive(int n) {
		long sum = 0;
		int k = 1;
		
		for (int i = 1 ; i < n + 1 ; i++) {
			sum += i;
			if (sum > n) {
				k = i - 1;
				break;
			}
		}
		
		return k;
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int n = scanner.nextInt();
		System.out.println(naive(n));
		
		scanner.close();
	}
}
