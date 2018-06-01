#include "stdafx.h"
#include "LongestCommonSubsequenceOfTwo.h"

using namespace std;

int dpLCS(int n, int* A, int m, int* B)
{
	int** result = new int*[n + 1];
	for (int i = 0; i < n + 1; i++)
		result[i] = new int[m + 1];

	for (int i = 0; i < n + 1; i++) {
		for (int j = 0; j < m + 1; j++) {
			if (i == 0 || j == 0) {
				result[i][j] = 0;
			}
			else {
				int insertion = result[i][j - 1];
				int deletion = result[i - 1][j];
				int mismatchOrMatch = result[i - 1][j - 1] + (A[i - 1] == B[j - 1] ? 1 : 0);

				result[i][j] = max({ insertion, deletion, mismatchOrMatch });
			}
		}
	}

	/*for (int i = 0; i < n + 1; i++) {
		for (int j = 0; j < m + 1; j++) {
			cout << result[i][j] << " ";
		}
		cout << endl;
	}*/

	return result[n][m];
}

LongestCommonSubsequenceOfTwo::LongestCommonSubsequenceOfTwo()
{
	/*int n, m;
	cin >> n;
	int* A = new int[n];
	for (int i = 0; i < n; i++)
		cin >> A[i];

	cin >> m;
	int* B = new int[m];
	for (int i = 0; i < m; i++)
		cin >> B[i];

	cout << dpLCS(n, A, m, B) << endl;*/

	ifstream file;
	file.open("C:/Users/sohee-um/program/git_repo/Algorithmic_Design_and_Techniques/sample/5_4_lcs2.in");
	if (!file) {
		cout << "cannot open a file!" << endl;
		exit(-1);
	}

	int n, m;
	file >> n;
	int* A = new int[n];
	for (int i = 0; i < n; i++)
		file >> A[i];

	file >> m;
	int* B = new int[m];
	for (int i = 0; i < m; i++)
		file >> B[i];

	cout << dpLCS(n, A, m, B) << endl;
}


LongestCommonSubsequenceOfTwo::~LongestCommonSubsequenceOfTwo()
{
}
