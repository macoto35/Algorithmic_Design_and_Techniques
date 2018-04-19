#include "stdafx.h"

using namespace std;

int memorySol(int n)
{
	if (n <= 1)
		return n;

	vector<int> arr(n + 1);
	arr[0] = 0;
	arr[1] = 1;

	for (int i = 2; i < n + 1; i++) {
		arr[i] = (arr[i - 1] + arr[i - 2]) % 10;
	}

	return arr[n];
}

int alternativeSol(int n)
{
	if (n <= 1)
		return n;

	int previous = 0;
	int current = 1;
	int tmp = 0;

	for (int i = 2; i < n + 1; i++) {
		tmp = previous;
		previous = current;
		current = (tmp + current) % 10;
	}

	return current;
}

int start()
{
	cout << "Hello--------------------------------" << endl;
	/*int n = 0;
	cin >> n;
	cout << alternativeSol(n) << endl;
	cout << memorySol(n) << endl;*/

	int a = 0;
	int b = 0;
	for (int n = 1000000; n < 10000001; n++) {
		a = alternativeSol(n);
		b = memorySol(n);
		if (a == b) {
			cout << n << " - ok" << endl;
		} else {
			cout << n << " - fail (" << a << " / " << b << ")" << endl;
			break;
		}
	}

	return 0;
}
