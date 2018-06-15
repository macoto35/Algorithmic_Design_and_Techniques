#include "stdafx.h"
#include "maxValArithmeticExpression.h"

using namespace std;

int arithmeticOperator(int i, char oper, int j)
{
	if (oper == '+')
		return i + j;
	else if (oper == '-')
		return i - j;
	else if (oper == '*')
		return i * j;
}

int* minAndMax(int** m, int** M, vector<char> oper, int i, int j)
{
	int minVal = 99999;
	int maxVal = -99999;

	for (int k = i; k < j; k++) {
		int a = arithmeticOperator(M[i][k], oper[k], M[k + 1][j]);
		int b = arithmeticOperator(M[i][k], oper[k], m[k + 1][j]);
		int c = arithmeticOperator(m[i][k], oper[k], M[k + 1][j]);
		int d = arithmeticOperator(m[i][k], oper[k], m[k + 1][j]);

		minVal = min({ minVal, a, b, c, d });
		maxVal = max({ maxVal, a, b, c, d });
	}

	return new int[] { minVal, maxVal };
}

int parentheses(vector<int> num, vector<char> oper)
{
	int n = num.size();

	int** m = new int*[n];
	int** M = new int*[n];
	for (int i = 0; i < n; i++) {
		m[i] = new int[n];
		M[i] = new int[n];
	}

	for (int i = 0; i < n; i++) {
		m[i][i] = num[i];
		M[i][i] = num[i];
	}

	for (int s = 1; s < n; s++) {
		for (int i = 0; i < n - s; i++) {
			int j = s + i;
			int* result = minAndMax(m, M, oper, i, j);
			m[i][j] = result[0];
			M[i][j] = result[1];
		}
	}
	return M[0][n - 1];
}

maxValArithmeticExpression::maxValArithmeticExpression()
{
	string s = "";
	cin >> s;

	vector<int> num;
	vector<char> oper;

	for (int k = 0; k < s.length(); k++) {
		char c = s.at(k);
		if (k % 2 == 0)
			num.push_back(c - '0');
		else
			oper.push_back(c);
	}

	cout << parentheses(num, oper) << endl;
}


maxValArithmeticExpression::~maxValArithmeticExpression()
{
}
