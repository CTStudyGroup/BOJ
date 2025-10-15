#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e11

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int T;
string a, b, c;
bool visited[201][201];

void dfs(int idx1, int idx2) {
    if(visited[idx1][idx2]) return;     // 이미 방문한 경우

    visited[idx1][idx2] = true;

    if(a[idx1] == c[idx1 + idx2]) dfs(idx1 + 1, idx2);
    if(b[idx2] == c[idx1 + idx2]) dfs(idx1, idx2 + 1);
}

void input() {
    cin >> T;

    for(int i = 1; i <= T; i++) {
        cin >> a >> b >> c;
        memset(visited, 0, sizeof(visited));
        dfs(0, 0);

        if(visited[a.size()][b.size()]) cout << "Data set " << i << ": " << "yes" << endl;
        else cout << "Data set " << i << ": " << "no" << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
