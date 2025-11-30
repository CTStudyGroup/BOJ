#include <iostream>
#include <deque>

using namespace std;

int main() {
	int n;
	cin >> n;

	string str;
	for (int i = 0; i < n; i++) {
		char input;
		cin >> input;

		str += input;
	}

	string answer = "";
	int front = 0;
	int back = str.size() - 1;
	while (front <= back) {
		if (str[front] < str[back]) {
			answer.push_back(str[front++]);
		}
		else if (str[front] == str[back]) {
			int go = 0;

			int front_temp = front;
			int back_temp = back;
			while (front_temp < back_temp) {
				if (str[front_temp] < str[back_temp]) {
					go = 1;
					break;
				}
				else if (str[front_temp] > str[back_temp]) {
					go = -1;
					break;
				}

				front_temp++;
				back_temp--;
			}

			if (go == 1)
				answer.push_back(str[front++]);
			else
				answer.push_back(str[back--]);
		}
		else {
			answer.push_back(str[back--]);
		}
	}

	for (int i = 1; i <= answer.size(); i++) {
		cout << answer[i - 1];
		if (i % 80 == 0) {
			cout << "\n";
		}
	}

	return 0;
}