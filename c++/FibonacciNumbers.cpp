#include "stdafx.h"
#include "FibonacciNumbers.h"

using namespace std;

double naiveSol(int n)
{
	if (n <= 1) {
		return n;
	}

	return naiveSol(n - 1) + naiveSol(n - 2);
}

double fastSol(int n)
{
	vector<double> arr(n + 1);
	arr[0] = 0;
	
	if (n > 0) {
		arr[1] = 1;
	}

	for (int i = 2; i < n + 1; i++) {
		arr[i] = arr[i - 1] + arr[i - 2];
	}

	return arr[n];
}

FibonacciNumbers::FibonacciNumbers()
{
	cout << "Hello----------------------" << endl;
	int n = 0;
	// cin >> n;

	// cout << naiveSol(n) << endl;
	// cout << fastSol(n) << endl;

	for (; n <= 45; n++) {
		assert(naiveSol(n) == fastSol(n));
		cout << n << endl;
	}
}


FibonacciNumbers::~FibonacciNumbers()
{
	cout << "Bye----------------------" << endl;
}
