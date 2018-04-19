#include "stdafx.h"

using namespace std;

int naive(long long n)
{
	if (n <= 1)
		return (int) n;

	int sum = 1;
	int prev = 0;
	int cur = 1;
	int tmp = 0;

	for (int i = 2; i < n + 1; i++)
	{
		tmp = prev;
		prev = cur;
		cur = (tmp + cur) % 10;
		sum = (sum + cur) % 10;
	}

	return sum;
}

int lastDigitFibo(long long n)
{
	vector<int> arr;
	arr.push_back(0);
	arr.push_back(1);
	int i = 2;

	while (true)
	{
		arr.push_back((arr[i - 1] + arr[i - 2]) % 10);
		if (arr[i - 1] == 0 && arr[i] == 1)
			break;
		else
			i++;
	}

	return arr[n % (i - 1)];
}

int fast(long long n)
{
	if (n <= 1)
		return (int) n;

	int val = lastDigitFibo(n + 2);

	return val > 0 ? val - 1 : 9;
}

int start()
{
	cout << "Hello--------------------------" << endl;
	long long n;
	cin >> n;
	cout << naive(n) << endl;
	cout << fast(n) << endl;

	return 0;
}

