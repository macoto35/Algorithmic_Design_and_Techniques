#include "stdafx.h"
#include "QuickSort.h"

using namespace std;

class MidPivot
{
public:
	int m1;
	int m2;
	MidPivot(int, int);
};

MidPivot::MidPivot(int a, int b)
{
	m1 = a;
	m2 = b;
}

void swapVal(int arr[], int i, int j)
{
	int tmp = arr[i];
	arr[i] = arr[j];
	arr[j] = tmp;
}

MidPivot partition(int arr[], int l, int r)
{
	int x = arr[l];
	int m1 = l, m2 = l;

	for (int i = l + 1; i < r; i++)
	{
		if (arr[i] < x)
		{
			m1 += 1;
			m2 += 1;
			swapVal(arr, m1, m2);
			swapVal(arr, m1, i);
		}
		else if (arr[i] == x)
		{
			m2 += 1;
			swapVal(arr, m2, i);
		}
	}
	swapVal(arr, l, m1);
	
	return MidPivot(m1, m2);
}

void findRandomPivot(int arr[], int l, int r)
{
	int m = l + floor((r - l) / 2);

	int a = arr[l];
	int b = arr[m];
	int c = arr[r];
	int mid = -1;

	if (a >= b && a >= c)
		mid = b >= c ? m : r ;

	if (b >= a && b >= c)
		mid = a >= c ? l : r;

	if (c >= a && c >= b)
		mid = a >= b ? l : m ;

	swapVal(arr, l, mid);
}

void sort(int arr[], int l, int r)
{
	while (l < r) {
		findRandomPivot(arr, l, r - 1);

		MidPivot midPivot = partition(arr, l, r);

		if ((midPivot.m1 - l) < (r - midPivot.m2))
		{
			sort(arr, l, midPivot.m1 - 1);
			l = midPivot.m2 + 1;
		}
		else
		{
			sort(arr, midPivot.m2 + 1, r);
			r = midPivot.m1 - 1;
		}
	}
}

QuickSort::QuickSort()
{
	int arr[] = { 1, 4, 2, 8, 7, 7, 9, 11 };
	sort(arr, 0, 7);

	for (int i = 0; i < 8; i++)
		cout << arr[i] << " ";
}


QuickSort::~QuickSort()
{
}
