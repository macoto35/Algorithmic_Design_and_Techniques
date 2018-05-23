#include "stdafx.h"
#include "MajorityElemt.h"

using namespace std;

int* swap(int* arr, int st, int m, int ed, int* a, int* b)
{
	if (a[0] != -1)
		for (int i = m + 1; i < ed + 1; i++)
			if (a[0] == arr[i])
				a[1] += 1;

	if (b[0] != -1)
		for (int i = st; i < m + 1; i++)
			if (b[0] == arr[i])
				b[1] += 1;

	int majorityCnt = floor((ed - st + 1) / 2);

	if (a[1] > majorityCnt)
		return a;
	else if (b[1] > majorityCnt)
		return b;
	else
		return new int[]{-1, 0};
}

int* merge(int* arr, int st, int m, int ed, int* a, int* b)
{
	if (a[0] == b[0])
	{
		a[1] += b[1];
		return a;
	}

	return swap(arr, st, m, ed, a, b);
}

int* findMajorityElemt(int* arr, int st, int ed)
{
	if (st == ed)
		return new int[]{arr[st], 1};

	int m = floor(st + (ed - st) / 2);

	int* a = findMajorityElemt(arr, st, m);
	int* b = findMajorityElemt(arr, m + 1, ed);

	return merge(arr, st, m, ed, a, b);
}

MajorityElemt::MajorityElemt()
{
	/*int n;
	cin >> n;

	int* arr = new int[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	int* result = findMajorityElemt(arr, 0, n - 1);
	cout << result[0] << '/' << result[1] << endl;*/

	ifstream file;
	file.open("./sample/4_2_majority_element.in");
	if (!file)
	{
		cout << "Unable to open this file!" << endl;
		exit(0);
	}

	int n;
	file >> n;

	int* arr = new int[n];
	for (int i = 0; i < n; i++)
		file >> arr[i];

	int* result = findMajorityElemt(arr, 0, n - 1);
	cout << result[0] << '/' << result[1] << endl;
}


MajorityElemt::~MajorityElemt()
{

}
