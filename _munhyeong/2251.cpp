#include <iostream>
#include <queue>
#include <set>

using namespace std;

struct Node {
	int a;
	int b;
	int c;

	bool operator<(const Node& other) const {
		if (a != other.a) return a < other.a;
		if (b != other.b) return b < other.b;
		return c < other.c;
	}
};

void insert_queue(queue<Node>& q, set<Node> &visited, int a, int b, int c) {
	if (visited.insert({ a, b, c }).second) {
		q.push({ a, b, c });
	}
}

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	
	set<Node> visited;
	queue<Node> q;

	q.push({ 0, 0, c });
	visited.insert(q.front());

	set<int> answer;
	while (!q.empty()) {
		Node front = q.front();
		q.pop();

		if (!front.a)
			answer.insert(front.c);
		// cout << front.a << " " << front.b << " " << front.c << "\n";

		int move;
		// a -> b
		move = min(front.a, (b - front.b));
		insert_queue(q, visited, front.a - move, front.b + move, front.c);

		// a -> c
		move = min(front.a, (c - front.c));
		insert_queue(q, visited, front.a - move, front.b, front.c + move);

		// b -> a
		move = min(front.b, (a - front.a));
		insert_queue(q, visited, front.a + move, front.b - move, front.c);

		// b -> c
		move = min(front.b, (c - front.c));
		insert_queue(q, visited, front.a, front.b - move, front.c + move);

		// c -> a
		move = min(front.c, (a - front.a));
		insert_queue(q, visited, front.a + move, front.b, front.c - move);

		// c -> b
		move = min(front.c, (b - front.b));
		insert_queue(q, visited, front.a, front.b + move, front.c - move);
	}
	
	for (auto e : answer)
		cout << e << " ";

	return 0;
}
