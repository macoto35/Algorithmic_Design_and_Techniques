#include "stdafx.h"
#include "BinarySearch.h"

using namespace std;

int binarySearch(vector<int> &arr, int low, int high, int key)
{
	if (low > high)
		return -1;

	int mid = floor(low + (high - low) / 2);

	if (key == arr[mid])
		return mid;
	else if (key < arr[mid])
		return binarySearch(arr, low, mid - 1, key);
	else
		return binarySearch(arr, mid + 1, high, key);
}

BinarySearch::BinarySearch()
{
	cout << "enter binary search" << endl;
	/*int tmp = 0;

	int n;
	cin >> n;
	vector<int> A;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		A.push_back(tmp);
	}

	int k;
	cin >> k;
	vector<int> B;
	for (int i = 0; i < k; i++)
	{
		cin >> tmp;
		B.push_back(tmp);
	}

	int cnt = 0;
	for (vector<int>::iterator it = B.begin(); it != B.end(); it++)
		if (binarySearch(A, 0, n - 1, *it) > -1)
			cnt += 1;

	cout << cnt << endl;*/

	ifstream file;
	file.open("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/4_1_binary_search.in");
	if (!file) 
	{
		cout << "Unable to open the file!" << endl;
		exit(1);
	}

	int tmp = 0;

	int n;
	file >> n;
	vector<int> A;
	for (int i = 0; i < n; i++)
	{
		file >> tmp;
		A.push_back(tmp);
	}

	int k;
	file >> k;
	vector<int> B;
	for (int i = 0; i < k; i++)
	{
		file >> tmp;
		B.push_back(tmp);
	}

	int cnt = 0;
	for (vector<int>::iterator it = B.begin(); it != B.end(); it++)
		if (binarySearch(A, 0, n - 1, *it) > -1)
			cnt += 1;

	cout << cnt << endl;

}


BinarySearch::~BinarySearch()
{
}
