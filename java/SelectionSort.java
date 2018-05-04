package algo;

public class SelectionSort {

	private static void swap(int[] arr, int i, int j) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
	
	private static void selectionSort(int[] arr) {
		int minIdx = 0;
		
		for(int i = 0 ; i < arr.length; i++) {
			minIdx = i;
			for(int j = i ; j < arr.length ; j++) {
				if (arr[j] < arr[minIdx])
					minIdx = j;
			}
			swap(arr, i, minIdx);
		}
	}
	
	public static void main(String[] args) {
		int arr[] = {8,4,2,5,2};
		selectionSort(arr);
		
		for(int i : arr)
			System.out.print(i + " ");
	}
}
