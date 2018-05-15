import java.util.*;

public class HugeFiboNumMod {

	private static int naive(long n, int m) {
		if (n <= 1)
			return (int) n;
		
		int previous = 0;
		int current = 1;
		int tmp = 0;
		for (long i = 2 ; i < n + 1 ; i++) {
			tmp = previous;
			previous = current;
			current = (tmp + current)  % m;
		}

		return current;
	}
	
	private static int fast(long n, int m) {
		if (n <= 1)
			return (int) n;
		
		List<Integer> arr = new ArrayList<Integer>();
		arr.add(0);
		arr.add(1);
		
		int i = 2;
		while(true) {
			arr.add( (arr.get(i - 1) + arr.get(i - 2)) % m );
			if (arr.get(i - 1) == 0 && arr.get(i) == 1)
				break;
			else
				i++;
		}
		
		int idx = (int) (n % (i - 1));		
		return arr.get( idx );
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		long n = scanner.nextLong();
		int m = scanner.nextInt();
		// System.out.println(naive(n, m));
		System.out.println(fast(n, m));
		
		/*Random rand = new Random();
		while(true) {
			long i = 1 + (long) (Math.random() * n);
			int j = rand.nextInt(m) + 2;
			System.out.print(i + "/" + j);

			if (naive(i, j) == fast(i, j)) {
				System.out.println(" - ok");
			} else {
				System.out.println(" - fail");
				break;
			}
		}*/
		
		scanner.close();
	}
}
