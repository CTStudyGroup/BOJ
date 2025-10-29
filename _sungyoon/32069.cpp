#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
    int r;
};

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {-1, 1};
ll L, N, K;     // 거리, 가로등, 출력 개수
queue<pair<ll, ll>> q;
set<ll> visited;

void bfs() {
    while(!q.empty()) {
        ll locate = q.front().first;
        ll dist = q.front().second;
        q.pop();

        cout << dist << endl;
        K--;

        if(K == 0) {
            return;
        }

        for(int i = 0; i < 2; i++) {
            ll nextlocate = locate + dx[i];
            ll nextdist = dist+1;

            if(nextlocate >= 0 && nextlocate <= L && !visited.count(nextlocate)) {
                q.push({nextlocate, nextdist});
                visited.insert(nextlocate);
            }
        }
    }
}

void solve() {
    bfs();
}

void input() {
    cin >> L >> N >> K;

    for(int i = 0; i < N; i++) {
        ll a;
        cin >> a;
        q.push({a, 0});
        visited.insert(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

