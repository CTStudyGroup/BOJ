#include <iostream>
#include <string>
#include <math.h>

using namespace std;

void print(int degree, int value, int preV, char variable) {
	if (value == 0)
		return;

	if (degree == 1)
		value /= 2;

	if (value == -1)
		cout << '-';
	else if (degree != 1 && preV != 0 && value > 0)
		cout << '+';

	if (abs(value) != 1)
		cout << value;
	for (int i = 0; i < degree + 1; i++)
		cout << variable;
}

int main() {
	string str;
	cin >> str;

	int coefficient = 0, idx = 0;
	string temp = "";
	while (idx < str.size()) {
		if (str[idx] == 'x') {
			coefficient = stoi(str.substr(0, idx));
			break;
		}
		temp += str[idx++];
	}
	if (coefficient == 0)
		idx = 0;

	print(1, coefficient, -1, 'x');

	bool is_not_zero = (coefficient != 0);
	int constant = 0;
	// 상수가 없는 경우를 나누고 싶음
	if (str.size() == 1 || idx != str.size() - 1) { 
		constant = stoi(str.substr(idx + is_not_zero));
		print(0, constant, coefficient, 'x');
	}

	print(0, 1, constant+coefficient, 'W');

	return 0;
}