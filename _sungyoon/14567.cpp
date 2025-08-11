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

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int N, M;
int arr[1001];
int isDegree[1001];
vector<vector<int>> v(1001);

void topologySort() {
    queue<pii> q;

    int cnt = 1;

    for(int i = 1; i <= N; i++) {
        if(isDegree[i] == 0) {
            q.push({i, cnt});
        }
    }

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        arr[x] = y;
        q.pop();

        for(auto it : v[x]) {
            if(--isDegree[it] == 0) {
                q.push({it, y+1});
            }
        }
    }

    for(int i = 1; i <= N; i++) {
        cout << arr[i] << " ";
    }
}

void solve() {
    topologySort();
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        isDegree[b]++;
        v[a].push_back(b);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
