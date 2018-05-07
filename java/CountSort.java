package algo;

public class CountSort {

	private static int[] countSort(int[] arr, int M) {
		int[] count = new int[M];
		for (int i = 0 ; i < arr.length ; i++)
			count[arr[i]] += 1;
		
		int[] pos = new int[M];
		for (int j = 1 ; j < M ; j++)
			pos[j] = pos[j - 1] + count[j - 1];
		
		int[] ret = new int[arr.length];
		for (int i = 0 ; i < arr.length ; i++) {
			ret[pos[arr[i]]] = arr[i];
			pos[arr[i]] += 1;
		}
		
		return ret;
	}
	
	public static void main(String[] args) {
		int[] arr = {2,3,2,1,3,2,2,3,2,2,2,1};
		for (int i : countSort(arr, 4)) {
			System.out.print(i +  ",");
		}
	}
}
