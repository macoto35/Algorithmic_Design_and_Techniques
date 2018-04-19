#include "stdafx.h"


using namespace std;

long long naive(int a, int b)
{
	for (long i = 1; i < (long long) a * b + 1; i++)
		if (i % a == 0 && i % b == 0)
			return i;

	return (long long) a * b;
}

int GCD(int a, int b)
{
	if (b == 0)
		return a;
	return GCD(b, a % b);
}

long long fast(int a, int b)
{
	return (long long) a * b / GCD(a, b);
}

int start()
{
	cout << "Hello------------------------------" << endl;
	int a, b;
	cin >> a >> b;
	// cout << naive(a, b) << endl;
	cout << fast(a, b) << endl;

	return 0;
}
