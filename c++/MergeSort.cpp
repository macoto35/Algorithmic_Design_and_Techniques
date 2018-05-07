#include "stdafx.h"
#include "MergeSort.h"

using namespace std;

vector<int> mergeTwoSortedArray(vector<int> &A, vector<int> &B)
{
	vector<int> C;

	int idxA = 0, idxB = 0;
	while (A.size() > idxA && B.size() > idxB)
	{
		int a = A.at(idxA);
		int b = B.at(idxB);

		if (a <= b)
		{
			C.push_back(a);
			idxA++;
		}
		else
		{
			C.push_back(b);
			idxB++;
		}
	}

	for (int i = idxA; i < A.size(); i++)
	C.push_back(A.at(i));

	for (int i = idxB; i < B.size(); i++)
	C.push_back(B.at(i));

	return C;
}

vector<int> mergeSort(int arr[], int st, int ed)
{
	if (st == ed) {
		vector<int> ret;
		ret.push_back(arr[st]);
		return ret;
	}

	int m = st + floor((ed - st) / 2);

	vector<int> A = mergeSort(arr, st, m);
	vector<int> B = mergeSort(arr, m + 1, ed);
	return mergeTwoSortedArray(A, B);
}

MergeSort::MergeSort()
{
	int arr[] = { 7, 2, 5, 3, 7, 13, 1, 6 };
	vector<int> result = mergeSort(arr, 0, 7);

	for (vector<int>::iterator i = result.begin(); i < result.end() ; i++)
	{
		cout << *i << " ";
	}
}


MergeSort::~MergeSort()
{
}
