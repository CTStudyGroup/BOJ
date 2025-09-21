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

int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
int graph[51][51];
int M_graph[51][51];

void solve() {
    int answer = 0;

    for(int i = 0; i < N - 2; i++) {
        for(int j = 0; j < M - 2; j++) {
            if(graph[i][j] != M_graph[i][j]) {
                for(int k = i; k <= i + 2; k++) {
                    for(int l = j; l <= j + 2; l++) {
                        graph[k][l] = 1 - graph[k][l];
                    }
                }
                answer++;
            }
            else continue;
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(graph[i][j] != M_graph[i][j]) {
                cout << -1;
                return;
            }
        }
    }

    cout << answer;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < M; j++) {
            graph[i][j] = s[j] - '0';
        }
    }

    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < M; j++) {
            M_graph[i][j] = s[j] - '0';
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

