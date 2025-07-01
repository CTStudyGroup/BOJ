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

struct FISH {
    int x;
    int y;
    int Dir;
    bool live;
};

//int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int N;
int graph[2200][2200];
int answer[3];

void bt(int x, int y, int n) {
    int tmp = graph[x][y];
    bool issame = true;

    if(n == 1) {
        if(graph[x][y] == 0) answer[0]++;
        else if(graph[x][y] == 1) answer[1]++;
        else answer[2]++;
        return;
    }

    for(int i = x; i < x + n; i++) {
        for(int j = y; j < y + n; j++) {
            if(tmp != graph[i][j]) {
                issame = false;
                break;
            }
        }
        if(!issame) {
            break;
        }
    }

    if(!issame) {       // 같지 않은 경우
        int len = n / 3;
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                bt(x + i * len, y + j * len, len);
            }
        }
    }
    else {
        if(tmp == 0) answer[0]++;
        else if(tmp == 1) answer[1]++;
        else answer[2]++;
    }
}

void solve() {
    bt(0, 0, N);

    cout << answer[2] << "\n" << answer[0] << "\n" << answer[1];
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> graph[i][j];
        }
    }

    solve();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
