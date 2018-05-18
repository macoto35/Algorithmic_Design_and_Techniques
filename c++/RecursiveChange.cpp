#include "stdafx.h"
#include "RecursiveChange.h"

using namespace std;

int dpChanges(int money, int coins[])
{
	int* minChanges = new int[money + 1];
	minChanges[0] = 0;
	int numCoin = 0;

	for (int i = 1; i < money + 1; i++) {
		minChanges[i] = 99999999;
		for (int j = 0; j < 3; j++) {
			if (i >= coins[j]) {
				numCoin = minChanges[i - coins[j]] + 1;
				if (numCoin < minChanges[i])
					minChanges[i] = numCoin;
			}
		}
	}

	return minChanges[money];
}

RecursiveChange::RecursiveChange()
{
	int money;
	cin >> money;
	
	int coins[] = { 4, 3, 1 };

	cout << dpChanges(money, coins) << endl;
}


RecursiveChange::~RecursiveChange()
{
}
