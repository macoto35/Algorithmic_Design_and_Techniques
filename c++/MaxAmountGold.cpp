#include "stdafx.h"
#include "MaxAmountGold.h"

using namespace std;

int maxAmountGold(int W, int n, int* golds) {
	int** result = new int*[n + 1];
	for (int i = 0; i < n + 1; i++)
		result[i] = new int[W + 1];

	int value = 0;
	for (int i = 0; i < n + 1; i++) {
		value = 0;
		for (int w = 0; w < W + 1; w++) {
			if (i == 0 || w == 0) {
				result[i][w] = 0;
			}
			else {
				result[i][w] = result[i - 1][w];
				if (golds[i - 1] <= w) {
					value = result[i - 1][w - golds[i - 1]] + golds[i - 1];
					if (value > result[i][w])
						result[i][w] = value;
				}
			}
		}
	}

	return result[n][W];
}

MaxAmountGold::MaxAmountGold()
{
	int W, n;
	cin >> W >> n;

	int* golds = new int[n];
	for (int i = 0; i < n; i++)
		cin >> golds[i];

	cout << maxAmountGold(W, n, golds) << endl;

	/*ifstream file;
	file.open("./sample/6_1_knapsack.in");
	if (!file) {
		cout << "cannot open file!" << endl;
		exit(-1);
	}

	int W, n;
	file >> W >> n;

	int* golds = new int[n];
	for (int i = 0; i < n; i++)
		file >> golds[i];

	cout << maxAmountGold(W, n, golds) << endl;*/
}


MaxAmountGold::~MaxAmountGold()
{
}
