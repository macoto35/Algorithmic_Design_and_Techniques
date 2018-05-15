import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class BinarySearch {
	
	private static int binarySearch(int[] arr, int low, int high, int key) {
		if (low > high)
			return -1;
		
		int mid = (int) Math.floor(low + (high - low) / 2);
		
		if (key == arr[mid]) {
			return mid;
		} else if (key < arr[mid]) {
			return binarySearch(arr, low, mid - 1, key);
		} else {
			return binarySearch(arr, mid + 1, high, key);
		}
	}
	
	public static void main(String[] args) {
		/*Scanner scanner = new Scanner(System.in);
		
		int n = scanner.nextInt();
		int[] A = new int[n];
		for (int i = 0 ; i < n ; i++) {
			A[i] = scanner.nextInt();
		}
		
		int k = scanner.nextInt();
		int[] B = new int[k];
		for (int i = 0 ; i < k ; i++) {
			B[i] = scanner.nextInt();
		}
		
		for (int b : B) {
			System.out.print(binarySearch(A, 0, n - 1, b) + " ");
		}

		scanner.close();*/
		
		try {
			Scanner scanner = new Scanner(Files.newInputStream(Paths.get("./sample/4_1_binary_search.in")));

			int n = scanner.nextInt();
			int[] A = new int[n];
			for (int i = 0 ; i < n ; i++) {
				A[i] = scanner.nextInt();
			}
			
			int k = scanner.nextInt();
			int[] B = new int[k];
			for (int i = 0 ; i < k ; i++) {
				B[i] = scanner.nextInt();
			}
			
			int idx = 0;
			for (int b : B) {
				if ( binarySearch(A, 0, n - 1, b) > -1 )
					idx += 1;
			}
			System.out.println(idx);

			scanner.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}
