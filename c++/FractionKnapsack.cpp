#include "stdafx.h"
#include "FractionKnapsack.h"

using namespace std;

class Pair {
public:
	double v;
	double w;
	Pair() { v = 0; w = 0; }
	Pair(double i, double j) { v = i; w = j; }
};

bool comp(Pair &a, Pair &b)
{
	return a.v / a.w >  b.v / b.w;
}

double greedyFast(int W, vector<Pair> &items)
{
	double maxValue = 0;
	
	for (int i = 0; i < items.size(); i++)
	{
		if (W == 0)
			break;
		double a = min(items[i].w, (double) W);
		maxValue += a * items[i].v / items[i].w;
		W -= a;
	}

	return maxValue;
}

FractionKnapsack::FractionKnapsack()
{
	/*int n, W, v, w;
	cin >> n >> W;

	vector<Pair> items;
	for (int i = 0; i < n; i++) {
		cin >> v >> w;
		items.push_back(Pair(v, w));
	}
	
	sort(items.begin(), items.end(), comp);

	//for (vector<Pair>::iterator it = items.begin(); it != items.end(); it++) {
	//	cout << it->v << it->w << endl;
	//}

	cout << fixed << setprecision(4) << greedyFast(W, items) << endl;
	*/


	ifstream file;
	file.open("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/3_2_loot.in");
	if (!file) {
		cout << "Unable to open file!" << endl;
		exit(1);
	}

	int n, W, v, w;
	file >> n >> W;

	vector<Pair> items;
	for (int i = 0; i < n; i++) {
		file >> v >> w;
		items.push_back(Pair(v, w));
	}

	sort(items.begin(), items.end(), comp);

	cout << fixed << setprecision(4) << greedyFast(W, items) << endl;
}


FractionKnapsack::~FractionKnapsack()
{
}
