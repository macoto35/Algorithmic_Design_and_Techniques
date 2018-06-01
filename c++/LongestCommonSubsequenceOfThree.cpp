#include "stdafx.h"
#include "LongestCommonSubsequenceOfThree.h"

using namespace std;

int dpLCS(int n, int* A, int m, int* B, int l, int* C)
{
	int*** result = new int**[n + 1];
	for (int i = 0; i < n + 1; i++) {
		result[i] = new int*[m + 1];
		for (int j = 0; j < m + 1; j++) {
			result[i][j] = new int[l + 1];
		}
	}

	for (int i = 0; i < n + 1; i++) {
		for (int j = 0; j < m + 1; j++) {
			for (int k = 0; k < l + 1; k++) {
				if (i == 0 || j == 0 || k == 0) {
					result[i][j][k] = 0;
				}
				else {
					int a = result[i][j][k - 1];
					int b = result[i][j - 1][k];
					int c = result[i - 1][j][k];
					int d = result[i - 1][j - 1][k];
					int e = result[i][j - 1][k - 1];
					int f = result[i - 1][j][k - 1];
					int g = result[i - 1][j - 1][k - 1] + (A[i - 1] == B[j - 1] && B[j - 1] == C[k - 1]? 1 : 0);

					result[i][j][k] = max({ a, b, c, d, e, f, g });
				}
			}
		}
	}

	return result[n][m][l];
}

LongestCommonSubsequenceOfThree::LongestCommonSubsequenceOfThree()
{
	/*int n, m, l;
	cin >> n;
	int* A = new int[n];
	for (int i = 0; i < n; i++)
		cin >> A[i];

	cin >> m;
	int* B = new int[m];
	for (int i = 0; i < m; i++)
		cin >> B[i];

	cin >> l;
	int* C = new int[l];
	for (int i = 0; i < l; i++)
		cin >> C[i];

	cout << dpLCS(n, A, m, B, l, C) << endl;*/

	ifstream file;
	file.open("./sample/5_5_lcs3.in");
	if (!file) {
		cout << "cannot open file!" << endl;
		exit(-1);
	}

	int n, m, l;
	file >> n;
	int* A = new int[n];
	for (int i = 0; i < n; i++)
		file >> A[i];

	file >> m;
	int* B = new int[m];
	for (int i = 0; i < m; i++)
		file >> B[i];

	file >> l;
	int* C = new int[l];
	for (int i = 0; i < l; i++)
		file >> C[i];

	cout << dpLCS(n, A, m, B, l, C) << endl;
}


LongestCommonSubsequenceOfThree::~LongestCommonSubsequenceOfThree()
{
}
