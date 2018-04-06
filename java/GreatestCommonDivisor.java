package algo;

import java.util.*;

public class GreatestCommonDivisor {

	private static int naive(int a, int b) {
		if (b == 0)
			return a;
		
		int currentGcd = 1;
		
		for (int d = 2 ; d <= a && d <= b ; d++) {
			if (a % d == 0 && b % d == 0)
				currentGcd = d;
		}
		
		return currentGcd;
	}
	
	private static int euclidean(int a, int b) {
		if (b == 0)
			return a;
		
		return euclidean(b, a % b);
	}
		
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		
		System.out.println(naive(a, b));
		System.out.println(euclidean(a, b));
		
		scanner.close();
	}
}
