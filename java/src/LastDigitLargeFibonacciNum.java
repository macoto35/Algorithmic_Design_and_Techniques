import java.util.*;

public class LastDigitLargeFibonacciNum {
	
	private static int memorySol(int n) {
		if (n <= 1)
			return n;
		
		int[] arr = new int[n + 1];
		arr[0] = 0;
		arr[1] = 1;
		
		for (int i = 2 ; i < n + 1; i++) {
			arr[i] = (arr[i - 1] + arr[i - 2]) % 10;
		}
		
		return arr[n];
	}

	private static int alternativeSol(int n) {
		if (n <= 1)
			return n;
		
		int previous = 0;
		int current = 1;
		int tmp = 0;
		
		for (int i = 2 ; i < n + 1 ; i++) {
			tmp = previous;
			previous = current;
			current = (tmp + current) % 10;
		}
		
		return current;
	}

	public static void main(String[] args) {
		/*Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		System.out.println(alternativeSol(n) + " / " + memorySol(n));
		in.close();*/
		
		int a = 0;
		int b = 0;

		for(int n = 100000 ; n < 1000001 ; n++) {
			a = alternativeSol(n);
			b = memorySol(n);
			
			if (a == b) {
				System.out.println(n + " - ok");
			} else {
				System.out.println(n + " - fail (" + a + "/" + b + ")");
				break;
			}
		}
	}
}
