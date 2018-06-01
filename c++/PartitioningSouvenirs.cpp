#include "stdafx.h"
#include "PartitioningSouvenirs.h"

using namespace std;

int knapSackWithoutRepetitions(int W, vector<int> &values)
{
	int** result = new int*[values.size() + 1];
	for (int i = 0; i < values.size() + 1; i++) {
		result[i] = new int[W + 1];
	}

	for (int i = 0; i < values.size() + 1; i++) {
		int value = 0;
		for (int w = 0; w < W + 1; w++) {
			if (i == 0 || w == 0) {
				result[i][w] = 0;
			}
			else {
				result[i][w] = result[i - 1][w];
				if (values.at(i - 1) <= w) {
					value = result[i - 1][w - values.at(i - 1)] + values.at(i - 1);

					if (value > result[i][w])
						result[i][w] = value;
				}
			}
		}
	}

	int returnValue = result[values.size()][W];

	vector<int> used;
	int i = values.size();
	int w = W;
	while (i != 0 && w != 0) {
		int curVal = result[i][w];
		int preVal = result[i - 1][w];

		if (curVal != preVal) {
			w -= values.at(i - 1);
			used.push_back(--i);
		}
		else {
			i--;
		}
	}

	for (auto& item : used) {
		values.erase(values.begin() + item);
	}

	return returnValue;
}

int dpPartitioningSouvenirs(int n, vector<int> &values, int sum)
{
	if (sum % 3 != 0)
		return 0;

	int W = sum / 3;

	int W1 = knapSackWithoutRepetitions(W, values);
	int W2 = knapSackWithoutRepetitions(W, values);
	int W3 = 0;
	for (auto& item : values)
		W3 += item;

	if (W == W1 && W == W2 && W == W3)
		return 1;
	else
		return 0;
}

PartitioningSouvenirs::PartitioningSouvenirs()
{
	/*int n;
	cin >> n;

	vector<int> values;
	int value = 0;
	int sum = 0;
	for (int i = 0; i < n; i++) {
		cin >> value;
		values.push_back(value);
		sum += value;
	}

	cout << dpPartitioningSouvenirs(n, values, sum) << endl;*/

	ifstream file;
	file.open("C:/Users/sohee-um/program/git_repo/Algorithmic_Design_and_Techniques/sample/6_2_souvenirs.in");
	if (!file) {
		cout << "cannot open a file!" << endl;
		exit(-1);
	}

	while (!file.eof()) {
		int n;
		file >> n;

		if (n < 0) {
			break;
		}

		vector<int> values;
		int value = 0;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			file >> value;
			values.push_back(value);
			sum += value;
		}

		cout << dpPartitioningSouvenirs(n, values, sum);
	}
}


PartitioningSouvenirs::~PartitioningSouvenirs()
{
}
