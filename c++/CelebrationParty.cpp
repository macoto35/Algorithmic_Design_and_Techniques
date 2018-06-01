#include "stdafx.h"
#include "CelebrationParty.h"

using namespace std;

void greedy(vector<int> &ages)
{
	int left = 0, l = 0, r = 0;

	while (left < ages.size()) {
		l = ages[left];
		r = l + 2;

		while (left < ages.size() && ages[left] <= r) {
			cout << ages[left] << ",";
			left += 1;
		}
		cout << endl;
	}
}

CelebrationParty::CelebrationParty()
{
	int n = 0;
	cin >> n;
	vector<int> ages(n);
	for (int i = 0; i < n; i++)
		cin >> ages[i];

	greedy(ages);
}

CelebrationParty::~CelebrationParty()
{
}
