#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>

using namespace std;

struct Tree {
	int x;
	int y;
	int age;
};

bool compare(const Tree& tree1, const Tree& tree2) {
	return tree1.age < tree2.age;
}

int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N, M, K;
	cin >> N >> M >> K;

	vector<vector<int>> remain_food(N, vector<int>(N));
	vector<vector<int>> add_food(N, vector<int>(N));
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			cin >> add_food[y][x];
			remain_food[y][x] = 5;
		}
	}

	// r은 y값 / c는 x값 | 1부터 시작

	deque<Tree> trees(M);
	for (int i = 0; i < M; i++) {
		cin >> trees[i].y >> trees[i].x >> trees[i].age;
		trees[i].x -= 1;
		trees[i].y -= 1;
	}

	sort(trees.begin(), trees.end(), compare);
	for (int year = 0; year < K; year++) {

//	봄: 자신의 나이만큼 양분을 먹고, 나이 1 증가.
//    : 하나의 칸에 여러 나무가 있을 경우, 어린 나무부터
//	  : 못 먹으면 즉시 죽는다.
		deque<Tree> alive_trees;
		vector<Tree> die_trees;
		for (Tree &tree : trees) {
			if (tree.age <= remain_food[tree.y][tree.x]) {
				remain_food[tree.y][tree.x] -= tree.age;
				tree.age += 1;
				alive_trees.push_back(tree);
			}
			else {
				die_trees.push_back(
					{
						tree.x,
						tree.y,
						tree.age
					});
			}
		}
		trees = alive_trees;

//	여름: 봄에 죽은 나무가 양분으로 변함
//		: 나이를 2로 나눈 값이 양분으로 추가 된다. (버림)
		for (Tree tree : die_trees) {
			remain_food[tree.y][tree.x] += tree.age / 2;
		}

//	가을: 나무가 번식(나이가 5의 배수)
//		: 인접한 8개의 칸에 나무가 1인 나무가 생긴다.
		vector<Tree> add_trees;
		for (Tree tree : trees) {
			if (tree.age % 5 == 0) {
				for (int dir = 0; dir < 8; dir++) {
					int cy = tree.y + dy[dir];
					int cx = tree.x + dx[dir];

					if (cy < 0 || cx < 0 || cy >= N || cx >= N)
						continue;

					add_trees.push_back({ cx, cy, 1 });
				}
			}
		}

		for (Tree tree : add_trees)
			trees.push_front(tree);

//	겨울: 로봇이 돌아다니면서 땅에 양분을 추가
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				remain_food[y][x] += add_food[y][x];
			}
		}
	}

	cout << trees.size();

	return 0;
}