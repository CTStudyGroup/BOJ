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
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int graph[4][4];
set<string> st;
int startx, starty;

string calculate() {
    string s = "";
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            s += to_string(graph[i][j]);
        }
    }

    return s;
}

void bfs() {
    queue<tuple<string, int, int, int>> q;
    string vis = calculate();
    q.push({vis, startx, starty, 0});
    st.insert(vis);

    while(!q.empty()) {
        string stand = get<0>(q.front());
        int x = get<1>(q.front());
        int y = get<2>(q.front());
        int cnt = get<3>(q.front());
        q.pop();

        if(stand == "123456780") {
            cout << cnt;
            exit(0);
        }

        for(int i = 0; i < 4; i++) {
            string tmp = stand;
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= 3 || ny < 0 || ny >= 3) continue;

            int zeroidx = x * 3 + y;
            int changeidx = nx * 3 + ny;
            swap(tmp[zeroidx], tmp[changeidx]);

            if(st.find(tmp) == st.end()) {
                st.insert(tmp);
                q.push({tmp, nx, ny, cnt+1});
            }
        }
    }
}

void solve() {
    bfs();

    cout << -1;
}

void input() {
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            cin >> graph[i][j];

            if(graph[i][j] == 0) {
                startx = i;
                starty = j;
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

