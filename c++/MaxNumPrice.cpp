#include "stdafx.h"
#include "MaxNumPrice.h"

using namespace std;

int greedyMaxNumPrice(int n)
{
	long long sum = 0;
	int k = 1;

	for (int i = 1; i < n + 1; i++)
	{
		sum += i;
		if (sum > n) {
			k = i - 1;
			break;
		}
	}

	return k;
}

MaxNumPrice::MaxNumPrice()
{
	cout << "---------------------------enter max num price" << endl;
	int n;
	cin >> n;
	cout << greedyMaxNumPrice(n) << endl;
}

MaxNumPrice::~MaxNumPrice()
{
}