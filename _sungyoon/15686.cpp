#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
int graph[51][51];
vector<coordinate> house;
vector<coordinate> chicken;
vector<int> selected;
bool visited[13];
int result = MAX;

int calc_distance() {
    int total = 0;
    for (auto h : house) {
        int dist = MAX;
        for (int idx : selected) {
            auto c = chicken[idx];
            dist = min(dist, abs(h.x - c.x) + abs(h.y - c.y));
        }
        total += dist;
    }
    return total;
}

void bt(int idx, int cnt) {
    if (cnt == M) {
        result = min(result, calc_distance());
        return;
    }

    for (int i = idx; i < chicken.size(); i++) {
        if (!visited[i]) {
            visited[i] = true;
            selected.push_back(i);
            bt(i + 1, cnt + 1);
            selected.pop_back();
            visited[i] = false;
        }
    }
}

void solve() {
    bt(0, 0);

    cout << result;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> graph[i][j];

            if(graph[i][j] == 1) {
                house.push_back({i, j});
            }
            else if(graph[i][j] == 2) {
                chicken.push_back({i, j});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
