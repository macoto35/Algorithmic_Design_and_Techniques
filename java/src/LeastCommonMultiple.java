import java.util.Random;
import java.util.Scanner;

public class LeastCommonMultiple {

	private static long naive(int a, int b) {
		for (long i = 1 ; i < (long) a * b + 1 ; i++) {
			if (i % a == 0 && i % b == 0) {
				return i;
			}
		}
		
		return (long) a * b;
	}
	
	private static long fast(int a, int b) {
		return (long) a * b / GCD(a, b);
	}
	
	private static int GCD(int a, int b) {
		if (b == 0)
			return a;

		return GCD(b, a % b);
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		
		// System.out.println(naive(a, b));
		System.out.println(fast(a, b));
		scanner.close();
	}
	
	/*public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		
		Random rand = new Random();
		
		while(true) {
			int a = rand.nextInt(n) + 1;
			int b = rand.nextInt(n) + 1;
			System.out.print(a + "    " + b);

			if (naive(a, b) == fast(a, b)){
				System.out.println(" - ok");
			} else {
				System.out.println(" - fail");
				break;
			}
		}

		scanner.close();
	}*/
}
