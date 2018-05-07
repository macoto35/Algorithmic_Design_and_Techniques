#include "stdafx.h"
#include "CountSort.h"

using namespace std;

int* countSort(int arr[], int n, int M)
{
	int* count = new int[M];
	int* pos = new int[M];

	for (int i = 0; i < M; i++) {
		count[i] = 0;
		pos[i] = 0;
	}

	for (int i = 0; i < n; i++)
		count[arr[i]] += 1;

	for (int j = 1; j < M; j++)
		pos[j] = pos[j - 1] + count[j - 1];

	int* result = new int[n];
	for (int i = 0; i < n; i++) 
	{
		result[pos[arr[i]]] = arr[i];
		pos[arr[i]] += 1;
	}

	return result;
}

CountSort::CountSort()
{
	int arr[] = { 2, 3, 2, 1, 3, 2, 2, 3, 2, 2, 2, 1 };
	
	int* result = countSort(arr, 12, 4);
	for (int i = 0; i < 12; i++)
		cout << result[i] << endl;
}


CountSort::~CountSort()
{
}
