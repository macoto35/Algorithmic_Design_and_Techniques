#include "stdafx.h"
#include "EditDistanceTwoStrings.h"

using namespace std;

int dpEditDistanceTwoStrings(string s1, string s2, int M, int N)
{
	int** result = new int*[M + 1];
	for (int i = 0; i < M + 1; i++) {
		result[i] = new int[N + 1];
	}

	for (int i = 0; i < M + 1; i++) {
		for (int j = 0; j < N + 1; j++) {
			if (i == 0 || j == 0) {
				result[i][j] = i + j;
			}
			else {
				int insertion = result[i][j - 1] + 1;
				int deletion = result[i - 1][j] + 1;
				int mismatchOrMatch = result[i - 1][j - 1] + (s1.at(i - 1) == s2.at(j - 1) ? 0 : 1);

				result[i][j] = min({ insertion, deletion, mismatchOrMatch });
			}
		}
	}

	/*for (int i = 0; i < M + 1; i++) {
		for (int j = 0; j < N + 1; j++) {
			cout << result[i][j];
		}
		cout << endl;
	}*/

	return result[M][N];

}

EditDistanceTwoStrings::EditDistanceTwoStrings()
{
	/*string s1, s2;
	cin >> s1 >> s2;

	cout << dpEditDistanceTwoStrings(s1, s2, s1.size(), s2.size()) << endl;*/

	string s1, s2;
	ifstream file;
	file.open("./sample/5_3_edit_distance.in");
	if (!file) {
		cout << "cannot open a file!" << endl;
		exit(-1);
	}
	file >> s1 >> s2;
	cout << dpEditDistanceTwoStrings(s1, s2, s1.size(), s2.size()) << endl;

}


EditDistanceTwoStrings::~EditDistanceTwoStrings()
{
}
