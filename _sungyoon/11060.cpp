#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N;
int arr[1001];
bool visited[1001];

void bfs() {
    queue<tuple<int, int, int>> q;
    q.push(make_tuple(1, arr[1], 0));
    visited[1] = true;

    while(!q.empty()) {
        int xx = get<0>(q.front());
        int dist = get<1>(q.front());
        int cnt = get<2>(q.front());
        q.pop();

        if(xx == N) {
            cout << cnt;
            return;
        }

        for(int i = 1; i <= dist; i++) {
            int nx = xx + i;

            if(nx >= 1 && nx <= 1000) {
                if(!visited[nx]) {
                    q.push(make_tuple(nx, arr[nx], cnt+1));
                    visited[nx] = true;
                }
            }
        }
    }

    cout << -1;
}

void solution() {
    bfs();
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solution();
}

