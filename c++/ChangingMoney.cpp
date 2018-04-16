#include "stdafx.h"
#include "ChangingMoney.h"

using namespace std;

int naive(int m)
{
	int cnt = -1;

	for (int i = 0; i < m + 1; i++) 
		for (int j = 0; j < m + 1; j++) 
			for (int k = 0; k < m + 1; k++) 
				if ( i * 1 + j * 5 + k * 10 == m && (cnt > i + j + k || cnt < 0) ) 
					cnt = i + j + k;

	return cnt;
}

int greedy(int m)
{
	array<int, 3> arr = {10, 5, 1};
	int remain = m;
	int cnt = 0;
	
	for (auto it = arr.begin(); it != arr.end(); it++) {
		cnt += remain / *it;
		remain = remain % *it;
	}

	return cnt;
}

ChangingMoney::ChangingMoney()
{
	cout << "Hello--------------------------" << endl;
	int m;
	cin >> m;
	cout << naive(m) << endl;
	cout << greedy(m) << endl;
}


ChangingMoney::~ChangingMoney()
{
	cout << "Bye--------------------------" << endl;
}
