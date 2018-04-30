#include "stdafx.h"
#include "MultiplyPolynomial.h"

using namespace std;

int* mult(int a[], int b[], int n, int ai, int bi, int size)
{
cout << "enter: " << n << "/" << ai << "/" << bi << endl;
	int* r = new int[2 * n - 1];
	for (int i = 0; i < 2 * n - 1; i++)
		r[i] = 0;

	if (n == 1) {
		int val1 = size > ai ? a[ai] : 0;
		int val2 = size > bi ? b[bi] : 0;
		r[0] = val1 * val2;
cout << "return +++++++ " << ai << "/" << bi << "/" << r[0] << endl;
		return r;
	}

	int d = floor(n / 2);
	int idx = 0;

	int* d0e0 = mult(a, b, d, ai, bi, size);
	for (int i = 0; i < n - 1; i++)
	{
cout << "d0e0------------ " << i << "/" << idx << "/" << d0e0[idx] << endl;
		r[i] = d0e0[idx];
		idx++;
	}
	delete[] d0e0;

	idx = 0;
	int* d1e1 = mult(a, b, d, ai + d, bi + d, size);
	for (int i = n; i < 2 * n - 1; i++)
	{
cout << "d1e1------------  " << i << "/" << idx << "/" << d1e1[idx] << endl;
		r[i] = d1e1[idx];
		idx++;
	}
	delete[] d1e1;

	idx = 0;
	int* d0e1 = mult(a, b, d, ai, bi + d, size);
	int* d1e0 = mult(a, b, d, ai + d, bi, size);
	for (int i = d; i < d + n - 1; i++)
	{
cout << "d0e1 * d1e0------------ " << i << "/" << idx << "/" << d0e1[idx] << "/" << d1e0[idx] << endl;
		r[i] += d0e1[idx] + d1e0[idx];
		idx++;
	}
	delete[] d0e1;
	delete[] d1e0;

	return r;
}

MultiplyPolynomial::MultiplyPolynomial()
{
	cout << "multiply polynomial start:" << endl;

	int coefficient = 4;
	int a[] = { 3, 2, 5 };
	int b[] = { 5, 1, 2 };

	int* result = mult(a, b, coefficient, 0, 0, 3);
	for (int i = 0; i < 2 * coefficient - 1 ; i++)
		cout << result[i] << endl;
	delete[] result;
}


MultiplyPolynomial::~MultiplyPolynomial()
{
}
