#include "stdafx.h"
#include "NumInversion.h"

using namespace std;

int sum = 0;

vector<int> merge(vector<int> &A, vector<int> &B)
{
	vector<int> C;
	int aIdx = 0;
	int bIdx = 0;

	while (A.size() > aIdx && B.size() > bIdx)
	{
		int a = A[aIdx];
		int b = B[bIdx];

		if (a <= b)
		{
			C.push_back(a);
			aIdx++;
		}
		else
		{
			C.push_back(b);
			bIdx++;

			sum += A.size() - aIdx;
		}
	}

	for (int i = aIdx; i < A.size(); i++)
		C.push_back(A[i]);

	for (int i = bIdx; i < B.size(); i++)
		C.push_back(B[i]);

	return C;
}

vector<int> numOfInversion(vector<int> &arr, int st, int ed)
{
	if (st == ed) {
		vector<int> ret;
		ret.push_back(arr[st]);
		return ret;
	}

	int m = st + floor((ed - st) / 2);
	
	vector<int> A = numOfInversion(arr, st, m);
	vector<int> B = numOfInversion(arr, m + 1, ed);
	return merge(A, B);
}

NumInversion::NumInversion()
{
	/*int n;
	cin >> n;

	vector<int> arr;
	int tmp = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		arr.push_back(tmp);
	}

	numOfInversion(arr, 0, n - 1);
	cout << sum << endl;*/

	ifstream file;
	file.open("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/4_4_inversions.in");
	
	int n;
	file >> n;

	vector<int> arr;
	int tmp = 0;
	for (int i = 0; i < n; i++)
	{
		file >> tmp;
		arr.push_back(tmp);
	}

	numOfInversion(arr, 0, n - 1);
	cout << sum << endl;

}


NumInversion::~NumInversion()
{
}
