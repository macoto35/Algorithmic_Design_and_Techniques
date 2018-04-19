#include "stdafx.h"
#include "MaxSalary.h"

using namespace std;

bool comp(string a, string b)
{
	return a + b > b + a;
}

string greedyMaxSalary(vector<string> &arr)
{
	string answer = "";

	while (arr.size() > 0)
	{
		string maxValue = "0";
		int idx = 0;

		for (int i = 0; i < arr.size(); i++)
		{
			if (comp(arr[i], maxValue))
			{
				maxValue = arr[i];
				idx = i;
			}
		}

		answer += maxValue;
		arr.erase(arr.begin() + idx);
	}

	return answer;
}

MaxSalary::MaxSalary()
{
	cout << "Max Salary" << endl;
	int n;
	cin >> n;

	vector<string> arr;
	string tmp = "";
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		arr.push_back(tmp);
	}

	cout << greedyMaxSalary(arr) << endl;
}


MaxSalary::~MaxSalary()
{
}
