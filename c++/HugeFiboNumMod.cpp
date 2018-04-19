#include "stdafx.h"

using namespace std;

int naive(long long n, int m)
{
	if (n <= 1)
		return n;

	int tmp = 0;
	int previous = 0;
	int current = 1;
	
	for (long long i = 2; i < n + 1; i++) {
		tmp = previous;
		previous = current;
		current = (tmp + current) % m;
	}

	return current;
}

int fast(long long n, int m)
{
	if (n <= 1)
		return n;

	vector<int> arr;
	arr.push_back(0);
	arr.push_back(1);
	long long i = 2;
	while (1) {
		arr.push_back((arr[i - 1] + arr[i - 2]) % m);
		if (arr[i - 1] == 0 && arr[i] == 1)
			break;
		else
			i++;
	}

	return arr[ (int)(n % (i - 1)) ];
}

int start()
{
	long long n;
	int m;
	cin >> n >> m;
	// cout << naive(n, m) << endl;
	cout << fast(n, m) << endl;

	return 0;
}

