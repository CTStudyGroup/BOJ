#include <iostream>
#include <math.h>

using namespace std;

struct Coord {
	long double y;
	long double x;
};

int main() {
	long long d;  string shape;
	long long x, y;
	cin >> d >> shape;
	cin >> x >> y;

	long double boundary = powl(2, d - 1);
	long double step = powl(2, d - 1);

	struct Coord cur = { 0, 0 };
	for (auto c : shape) {
		if (c == '1') {
			cur.x += step / 2;
			cur.y += step / 2;
		}
		else if (c == '2') {
			cur.x -= step / 2;
			cur.y += step / 2;
		}
		else if (c == '3') {
			cur.x -= step / 2;
			cur.y -= step / 2;
		}
		else {
			cur.x += step / 2;
			cur.y -= step / 2;
		}

		step /= 2;
	}
	cur.x += x;
	cur.y += y;
	if (boundary < abs(cur.y) || boundary < abs(cur.x)) {
		cout << -1;
		return 0;
	}

	string answer = "";
	step = powl(2, d - 1);
	Coord point = { 0, 0 };
	for (int i = 0; i < d; i++) {
		if (point.y < cur.y && point.x < cur.x) { // 1 사분면
			point.x += step / 2;
			point.y += step / 2;
			answer += "1";
		}
		else if (point.y < cur.y && point.x > cur.x) { // 2 사분면
			point.x -= step / 2;
			point.y += step / 2;
			answer += "2";
		}
		else if (point.y > cur.y && point.x > cur.x) { // 3 사분면
			point.x -= step / 2;
			point.y -= step / 2;
			answer += "3";
		}
		else { // 4 사분면
			point.x += step / 2;
			point.y -= step / 2;
			answer += "4";
		}

		step /= 2;
	}

	cout << answer;

	return 0;
}
