import java.util.*;

public class LastDigitOfSumOfFiboNum {

	private static int naive(long n) {
		if(n <= 1)
			return (int) n;
		
		long sum = 1;
		long prev = 0;
		long cur = 1;
		long tmp = 0;
		
		for (int i = 2 ; i < n + 1 ; i++) {
			tmp = prev;
			prev = cur;
			cur = (tmp + cur) % 10;
			sum = (sum + cur) % 10;
			// System.out.println(i + ":" + cur + "/" + sum);
		}
		
		return (int) sum;
	}
	
	private static int fast(long n) {
		if (n  <= 1)
			return (int) n;
		
		int val = lastDigitFibo(n + 2);
		
		return val > 0 ? val - 1 : 9;
	}
	
	private static int lastDigitFibo(long n) {
		List<Integer> arr = new ArrayList<>();
		arr.add(0);
		arr.add(1);
		int i = 2;
		
		while(true) {
			arr.add( (arr.get(i - 1) + arr.get(i - 2)) % 10 );
			if (arr.get(i - 1) == 0 && arr.get(i) == 1)
				break;
			else
				i++;
		}
		
		return arr.get( (int) (n % (i - 1)) );
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		long n = scanner.nextLong();
		// System.out.println(naive(n));
		System.out.println(fast(n));
		
		/*long N = scanner.nextLong();
		while(true) {
			long n =  (long) (Math.random() * (N + 1));
			if (naive(n) == fast(n)) {
				System.out.println(n + "  - ok");				
			} else {
				System.out.println(n + "  - fail");
				break;
			}
		}*/
		
		scanner.close();
	}
}
