#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    string s;
    vector<int> v;
};

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int N, M;
int graph[51][51];
int arr[2501];
int dp[51][51];
int cnt = 1;

/*
    1. 방의 개수 -> set사용
    2. 가장 넓은 방의 넓이  -> 크기만큼 리턴
    3. 
*/

void bfs(int a, int b) {
    queue<pii> q;
    q.push({a, b});
    dp[a][b] = cnt;
    int count = 1;

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            if (!(graph[x][y] & (1 << i))) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx >= 0 && nx < M && ny >= 0 && ny < N) {
                    if(!dp[nx][ny]) {
                        dp[nx][ny] = cnt;
                        q.push({nx, ny});
                        count++;
                    }
                }
            }
        }
    }
    arr[cnt] = count;
}

void solve() {

    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++) {
            if(dp[i][j] == 0) {
                bfs(i, j);
                cnt++;
            }
        }
    }

    int answer3 = 0;

    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++) {
            for(int k = 0; k < 4; k++) {
                set<int> st;
                st.insert(dp[i][j]);
                int nx = i + dx[k];
                int ny = j + dy[k];

                if(nx >= M || nx < 0 || ny >= N || ny < 0) continue;

                if(dp[i][j] != dp[nx][ny]) {
                    int tmpsz = arr[dp[i][j]] + arr[dp[nx][ny]];
                    answer3 = max(answer3, tmpsz);
                }
            }
        }
    }

    int answer2 = 0;

    for(int i = 1; i < cnt; i++) {
        answer2 = max(answer2, arr[i]);
    }

    cout << cnt-1 << endl << answer2 << endl << answer3 << endl;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < M; i++) {
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
