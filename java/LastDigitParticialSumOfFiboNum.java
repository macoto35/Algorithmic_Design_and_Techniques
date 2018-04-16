package algo;

import java.util.*;

public class LastDigitParticialSumOfFiboNum {

	private static int naive(long m, long n) {
		int sum = 0;
		int cur = 0;
		int next = 1;
		int tmp = 0;
		
		for (long i = 0 ; i < n + 1 ; i++) {
			if (i >= m)
				sum = (sum + cur) % 10;
			tmp = cur;
			cur = next;
			next = (tmp + next) % 10; 
		}
		
		return sum;
	}
	
	private static int fast(long m, long n) {
		int allSum = getFiboSum(n + 2);
		int prevSum = getFiboSum(m + 1);
		int partSum = allSum - prevSum;

		return partSum < 0 ? partSum + 10 : partSum;
	}
	
	private static int getFiboSum(long n) {
		List<Integer> arr = new ArrayList<Integer>();
		arr.add(0);
		arr.add(1);
		int i = 2;
		while(true) {
			arr.add( (arr.get(i - 1) + arr.get(i - 2)) % 10 );
			if (arr.get(i-1) == 0 && arr.get(i) == 1)
				break;
			else
				i++;
		}
		
		int val = arr.get( (int) (n % (i - 1)) );
		return val == 0 ? 9 : val - 1;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		
		long m = scanner.nextLong();
		long n = scanner.nextLong();
		// System.out.println(naive(m, n));
		System.out.println(fast(m, n));
		
		
		/*long N = scanner.nextLong();
		
		while(true) {
			long a = (long) (Math.random() * (N + 1));
			long b = (long) (Math.random() * (N + 1));
			long m = Math.min(a, b);
			long n = Math.max(a, b);
			
			if (naive(m, n) == fast(m, n)) {
				System.out.println(m + "/" + n + " - ok");
			} else {
				System.out.println(m + "/" + n + " - fail");
				break;
			}
		}*/
				
		scanner.close();
	}
}
