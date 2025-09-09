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
int T, answer;
bool visited[11];

void bt(int x, int cnt, vector<vector<int>> &graph, int val) {
    if(cnt == 11) {
        answer = max(answer, val);
        return;
    }

    for(int i = 0; i < 11; i++) {
        if(graph[x][i] > 0 && !visited[i]) {
            visited[i] = true;
            bt(x+1, cnt+1, graph, val + graph[x][i]);
            visited[i] = false;
        }
    }
}

void solve(vector<vector<int>> &graph) {
    bt(0, 0, graph, 0);

    cout << answer << endl;
}

void input() {
    cin >> T;

    while(T--) {
        answer = 0;
        vector<vector<int>> v(11, vector<int>(11, 0));

        for(auto &it : v) {
            for(auto &iter : it) {
                cin >> iter;
            }
        }

        solve(v);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

