#include "stdafx.h"

using namespace std;

bool comp(long long a, long long b)
{
	return a > b;
}

long long greedy(int n, vector<long long> &a, vector<long long> &b)
{
	long long sum = 0;
	
	for (int i = 0; i < n; i++)
		sum += a[i] * b[i];

	return sum;
}

int start()
{
	/*int n;
	cin >> n;

	vector<long> a;
	vector<long> b;
	long tmp;

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		a.push_back(tmp);
	}

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		b.push_back(tmp);
	}

	sort(a.begin(), a.end(), comp);
	sort(b.begin(), b.end(), comp);

	cout << greedy(n, a, b) << endl;*/

	ifstream file;
	file.open("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/3_3_dot_product20180216.in");
	if (!file) {
		cout << "Unable to open file!" << endl;
		exit(1);
	}

	int n;
	file >> n;

	vector<long long> a;
	vector<long long> b;
	long long tmp;

	for (int i = 0; i < n; i++) {
		file >> tmp;
		a.push_back(tmp);
	}

	for (int i = 0; i < n; i++) {
		file >> tmp;
		b.push_back(tmp);
	}

	sort(a.begin(), a.end(), comp);
	sort(b.begin(), b.end(), comp);

	cout << greedy(n, a, b) << endl;

	return 0;
}
