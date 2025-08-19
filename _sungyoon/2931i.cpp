#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

//int dx[] = {0, 1, -1, 0,1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
//int dx[] = {-1, 0, 1, 0};       // 시계방향
//int dy[] = {0, 1, 0, -1};
int N, M;
char graph[26][26];
pii result;
map<char, vector<vector<int>>> m = {
        { '|', {{-1, 0}, {1, 0}} },
        { '-', {{0, -1}, {0, 1}} },
        { '+', {{-1, 0}, {0, 1}, {1, 0}, {0, -1}} },
        { '1', {{1, 0}, {0, 1}} },
        { '2', {{-1, 0}, {0, 1}} },
        { '3', {{-1, 0}, {0, -1}} },
        { '4', {{0, -1}, {1, 0}} }
};

void solve() {
    vector<vector<int>> v;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if (graph[i][j] != '.') {
                int x = i;
                int y = j;
                if(m.find(graph[i][j]) != m.end()) {        // 있는 경우
                    for(auto it : m[graph[i][j]]) {
                        int nx = x + it[0];
                        int ny = y + it[1];

                        if(graph[nx][ny] == '.') {
                            result.first = nx+1;
                            result.second = ny+1;
                            v.push_back({it[0] * -1, it[1] * -1});
                        }
                    }
                }
            }
        }
    }
    sort(v.begin(), v.end());
    if(v.size() == 4) {
        cout << result.first << " " << result.second << " " << '+';
        return;
    }
    else {
        for(auto it : m) {
            vector<vector<int>> stand = it.second;
            sort(stand.begin(), stand.end());

            if(stand == v) {
                cout << result.first << " " << result.second << " " << it.first;
                return;
            }
        }
    }
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < M; j++) {
            graph[i][j] = s[j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
