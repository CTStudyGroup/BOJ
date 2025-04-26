#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N, M;
char graph[51][51];

void solve() {
    int stand = min(N, M);
    stand--;
    int result = 1;

    for(int k = 1; k <= stand; k++) {
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(i+k < N && j+k < M) {
                    if(graph[i][j] == graph[i+k][j] && graph[i+k][j] == graph[i][j+k] && graph[i][j+k] == graph[i+k][j+k]) {
                        result = max(result, (k+1) * (k+1));
                    }
                }
            }
        }
    }

    cout << result;
}

void input() {
    cin >> N >> M;

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
