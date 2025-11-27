#include <iostream>
#include <map>

using namespace std;

struct Node {
	map<string, Node *> children;
};

void traversal(Node root, int depth) {
	for (auto e : root.children) {
		for (int i = 0; i < depth; i++)
			cout << "--";
		cout << e.first << "\n";
		traversal(*(e.second), depth + 1);
	}
}

int main() {
	int N;
	cin >> N;

	string str;
	Node root;
	for (int i = 0; i < N; i++) {
		int K;
		cin >> K;

		Node* cur = &root;
		for (int j = 0; j < K; j++) {
			cin >> str;

			if (cur->children.find(str) != cur->children.end()) {
				//  존재
				cur = cur->children[str];
			}
			else {
				// 없는 경우
				Node* temp = new Node();
				cur->children[str] = temp;
				cur = temp;
			}
		}
	}

	traversal(root, 0);

	return 0;
}