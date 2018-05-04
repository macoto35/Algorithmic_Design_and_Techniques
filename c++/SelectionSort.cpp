#include "stdafx.h"
#include "SelectionSort.h"

using namespace std;

void swap(int arr[], int i, int j)
{
	int tmp = arr[i];
	arr[i] = arr[j];
	arr[j] = tmp;
}

void selectionSort(int arr[], int n)
{
	int minIdx = 0;

	for (int i = 0; i < n; i++) {
		minIdx = i;
		for (int j = i; j < n; j++)
			if (arr[j] < arr[minIdx])
				minIdx = j;
		swap(arr, i, minIdx);
	}
}

SelectionSort::SelectionSort()
{
	int arr[] = { 8, 4, 2, 5, 2 };
	selectionSort(arr, 5);

	for (int i = 0; i < 5; i++)
		cout << arr[i] << ' ';
}


SelectionSort::~SelectionSort()
{
}
