#include "stdafx.h"


using namespace std;

double naive(const vector<double> &numbers)
{
	int length = numbers.size();
	double product = 0;

	for (int i = 0; i < length; i++) {
		for (int j = i + 1; j < length; j++) {
			product = max(product, numbers[i] * numbers[j]);
		}
	}

	return product;
}

double fast(const vector<double> &numbers)
{
	double lg = 0;
	double secoundLg = 0;

	for (int i = 0; i < numbers.size(); i++) {
		if (lg < numbers[i]) {
			secoundLg = lg;
			lg = numbers[i];
		} else if (secoundLg < numbers[i]) {
			secoundLg = numbers[i];
		}
	}

	return lg * secoundLg;
}

double fastest(vector<double> &numbers)
{
	sort(numbers.begin(), numbers.end());
	int n = numbers.size();
	return numbers[n - 1] * numbers[n - 2];
}

int start()
{
	cout << "hello-----------------------------!" << endl;
	int n = 0;
	cin >> n;

	vector<double> numbers(n);
	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
	}

	cout << "naive result: " << naive(numbers) << endl;
	cout << "fast result: " << fast(numbers) << endl;
	cout << "fastest result: " << fastest(numbers) << endl;

	return 0;
}
