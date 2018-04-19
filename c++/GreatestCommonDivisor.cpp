#include "stdafx.h"

using namespace std;

int naive(int a, int b)
{
	if (b == 0)
		return a;

	int currentGcd = 1;
	for (int d = 2; d <= a && d <= b; d++) {
		if (a % d == 0 && b % d == 0) {
			currentGcd = d;
		}
	}

	return currentGcd;
}

int euclidean(int a, int b)
{
	if (b == 0)
		return a;

	return euclidean(b, a%b);
}

int start()
{
	cout << "Hello--------------------------------" << endl;
	int a = 0, b = 0;
	cin >> a;
	cin >> b;

	cout << naive(a, b) << endl;
	cout << euclidean(a, b) << endl;

	return 0;
}

