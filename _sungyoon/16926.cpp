#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M, R;
int graph[300][300];


void solve() {
    int lineCount = min(N, M) / 2;

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < lineCount; j++) {
            int tmp = graph[j][j];

            // 우측 상단 -> 좌측 상단
            for(int k = j + 1; k < M - j; k++) {
                graph[j][k-1] = graph[j][k];
            }

            // 우측 하단 -> 우측 상단
            for(int k = j + 1; k < N - j; k++) {
                graph[k-1][M-1-j] = graph[k][M-1-j];
            }

            // 좌측 하단 -> 우측 하단
            for(int k = M - 2 - j; k >= j; k--) {
                graph[N-1-j][k+1] = graph[N-1-j][k];
            }

            // 좌측 상단 -> 좌측 하단
            for(int k = N - j - 2; k >= j + 1; k--) {
                graph[k+1][j] = graph[k][j];
            }

            graph[j+1][j] = tmp;
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

void input() {
    cin >> N >> M >> R;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
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
