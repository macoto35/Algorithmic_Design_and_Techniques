#include "stdafx.h"
#include "PrimitiveCalculator.h"

using namespace std;

int dpCalculator(int num, int primitive[], int size)
{
	int* result = new int[num + 1];
	for (int i = 0; i < num + 1; i++)
	{
		if (i < 2)
			result[i] = 0;
		else
			result[i] = 99999;
	}

	for (int n = 2; n < num + 1; n++)
	{
		int minCnt = 99999;
		for (int i = 0; i < size; i++)
		{
			int p = primitive[i];
			if (n >= p)
			{
				if (p == 1)
					minCnt = result[n - 1] + 1;
				else if (n % p == 0)
					minCnt = result[n / p] + 1;
			}
			
			if (result[n] > minCnt)
				result[n] = minCnt;
		}
	}

	return result[num];
}

PrimitiveCalculator::PrimitiveCalculator()
{
	int n;
	cin >> n;

	int p[] = {1, 2, 3};

	cout << dpCalculator(n, p, 3) << endl;
}


PrimitiveCalculator::~PrimitiveCalculator()
{
}
