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
int N, K;
ll answer;
queue<pii> q;
set<int> st;

void bfs() {
    while(!q.empty()) {
        int x = q.front().first;
        int bad = q.front().second;
        q.pop();

        for(int i = 0; i < 2; i++) {
            int nx = x + dx[i];

            if(st.count(nx) == 0) {
                q.push({nx, bad+1});
                answer += bad + 1;
                K--;
                st.insert(nx);
            }

            if(!K) {
                cout << answer;
                return;
            }
        }
    }
}

void solve() {
    bfs();
}

void input() {
    cin >> N >> K;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        q.push({a, 0});
        st.insert(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

