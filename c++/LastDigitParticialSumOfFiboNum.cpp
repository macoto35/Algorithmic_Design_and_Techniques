#include "stdafx.h"
#include "LastDigitParticialSumOfFiboNum.h"

using namespace std;

int naive(long long m, long long n)
{
	int sum = 0;
	int cur = 0;
	int next = 1;
	int tmp = 0;

	for (long long i = 0; i < n + 1; i++)
	{
		if (i >= m)
			sum = (sum + cur) % 10;

		tmp = cur;
		cur = next;
		next = (tmp + next) % 10;
	}

	return sum;
}

int getFibo(long long n)
{
	vector<int> arr;
	arr.push_back(0);
	arr.push_back(1);
	int i = 2;

	while (true) {
		arr.push_back((arr[i - 1] + arr[i - 2]) % 10);
		if (arr[i - 1] == 0 && arr[i] == 1)
			break;
		else
			i++;
	}

	int val = arr[n % (i - 1)];
	return val < 0 ? 9 : val - 1;
}

int fast(long long m, long long n)
{
	int allSum = getFibo(n + 2);
	int prevSum = getFibo(m + 1);
	int partSum = getFibo(n + 2) - getFibo(m + 1);

	return partSum < 0 ? partSum + 10 : partSum;
}

LastDigitParticialSumOfFiboNum::LastDigitParticialSumOfFiboNum()
{
	cout << "Hello-----------------------------" << endl;
	long long m, n;
	cin >> m >> n;
	cout << naive(m, n) << endl;
	cout << fast(m, n) << endl;
}


LastDigitParticialSumOfFiboNum::~LastDigitParticialSumOfFiboNum()
{
	cout << "Bye------------------------------" << endl;
}
