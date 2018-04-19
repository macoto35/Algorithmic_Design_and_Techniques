#include "stdafx.h"

using namespace std;

class Time
{
public:
	int x;
	int y;
	Time() { x = 0; y = 0; }
	Time(int i, int j) { x = i; y = j; }
};

bool comp(Time &a, Time &b)
{
	return a.y < b.y;
}

int greedy(vector<Time> &arr)
{
	int maxRightPoint = 0;
	vector<int> res;

	while (arr.size() > 0)
	{
		res.push_back(arr[0].y);
		maxRightPoint = arr[0].y;

		//arr.erase(remove_if(arr.begin(), arr.end(), [](Time item) { return item.x > maxRightPoint || item.y < maxRightPoint; }), arr.end());
		vector<Time>::iterator it = arr.begin();
		while (it != arr.end()) {
			if ((*it).x <= maxRightPoint && (*it).y >= maxRightPoint)
				it = arr.erase(it);
			else
				++it;
		}
	}

	return res.size();
}

int start()
{
	/*int n;
	cin >> n;

	int x, y;
	vector<Time> arr;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		arr.push_back(Time(x, y));
	}

	sort(arr.begin(), arr.end(), comp);

	cout << greedy(arr) << endl;*/

	ifstream file;
	file.open("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/3_4_covering_segments.in");
	if (!file) {
		cout << "Unable to open file!" << endl;
		exit(1);
	}
	
	int n;
	file >> n;

	int x, y;
	vector<Time> arr;
	for (int i = 0; i < n; i++) {
		file >> x >> y;
		arr.push_back(Time(x, y));
	}

	sort(arr.begin(), arr.end(), comp);

	cout << greedy(arr) << endl;
	
	return 0;
}

