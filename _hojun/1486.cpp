#include <bits/stdc++.h>
using namespace std;

#define INF 1e9

int n, m, T, D;
int direction[4][2] = { {0,1},{0,-1},{1,0},{-1,0} };
vector<vector<int>> M;

struct Point {
    int x, y;
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
};

vector<vector<int>> dijkstra(int sx, int sy, bool bIsClimb) {
    vector<vector<int>> dist(n, vector<int>(m, INF));
    priority_queue<pair<int, Point>, vector<pair<int, Point>>, greater<pair<int, Point>>> pq;

    dist[sx][sy] = 0;
    pq.push({ 0, {sx, sy} });

    while (!pq.empty()) {
        int curCost = pq.top().first;
        Point p = pq.top().second;
        pq.pop();
        int x = p.x, y = p.y;

        if (dist[x][y] < curCost) continue;

        for (auto& d : direction) {
            int nx = x + d[0];
            int ny = y + d[1];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            int diff = M[nx][ny] - M[x][y];
            if (abs(diff) > T) continue;

            int nextCost = 0;

            if (bIsClimb) {
                if (diff <= 0) {
                    nextCost = curCost + 1;
                }
                else {
                    nextCost = curCost + pow(abs(diff), 2);
                }
            }
            else {
                if (diff >= 0) {
                    nextCost = curCost + 1;
                }
                else {
                    nextCost = curCost + pow(abs(diff), 2);
                }
            }

            if (nextCost < dist[nx][ny]) {
                dist[nx][ny] = nextCost;
                pq.push({ nextCost, {nx, ny} });
            }
        }
    }

    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> T >> D;
    M.assign(n, vector<int>(m));

    // 높이 입력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c; cin >> c;
            if (c >= 'a') c = c - 'a' + 26;
            else c = c - 'A';
            M[i][j] = c;
        }
    }

    auto dist_go = dijkstra(0, 0, true);
    auto dist_back = dijkstra(0, 0, false);

    int answer = -1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dist_go[i][j] + dist_back[i][j] <= D)
                answer = max(answer, M[i][j]);
        }
    }

    cout << answer;
}
