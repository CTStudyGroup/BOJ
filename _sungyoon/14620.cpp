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

struct nutrition {
    int p;
    int f;
    int s;
    int v;
    int cost;
};

int dx[] = {0 ,0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {0, -1, 0, 1, 0, -1, 1, -1, 1};
int N;
int graph[11][11];
bool visited[11][11];
int result = MAX;

bool cando(int x, int y) {
    for(int i = 0; i < 5; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx < 0 || nx >= N || ny < 0 || ny >= N) return false;

        if(visited[nx][ny]) return false;
    }
    return true;
}

int extractcost(int x, int y) {
    int cost = 0;

    for(int i = 0; i < 5; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        cost += graph[nx][ny];
    }

    return cost;
}

void placeflower(int x, int y, int status) {
    if(status == 0) {
        for(int i = 0; i < 5; i++) { 
            int nx = x + dx[i];
            int ny = y + dy[i];

            visited[nx][ny] = true;
        }
    }
    else {
        for(int i = 0; i < 5; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            visited[nx][ny] = false;
        }
    }
}

void bt(int cnt, int totalcost) {
    if(cnt == 3) {
        result = min(result, totalcost);
        return;
    }

    for(int i = 1; i < N-1; i++) {
        for(int j = 1; j < N-1; j++) {
            if(cando(i, j)) {
                placeflower(i, j, 0);
                int tmpcost = extractcost(i, j);
                bt(cnt+1, totalcost + tmpcost);
                placeflower(i, j, 1);
            }
        }
    }
}

void solve() {
    bt(0, 0);

    cout << result;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> graph[i][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

