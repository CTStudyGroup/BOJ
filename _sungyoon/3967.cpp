#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {0,-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0,0, 0, -1, 1, -1, 1, -1, 1};
char graph[6][10];
bool Select[13];
vector<pii> v;
int cnt;

bool checkstar() {
    if((graph[0][4] - 'A' + 1) + (graph[1][3] - 'A' + 1) + (graph[2][2] - 'A' + 1) + (graph[3][1] - 'A' + 1) != 26) return false;
    if((graph[3][1] - 'A' + 1) + (graph[3][3] - 'A' + 1) + (graph[3][5] - 'A' + 1) + (graph[3][7] - 'A' + 1) != 26) return false;
    if((graph[3][7] - 'A' + 1) + (graph[2][6] - 'A' + 1) + (graph[1][5] - 'A' + 1) + (graph[0][4] - 'A' + 1) != 26) return false;
    if((graph[1][1] - 'A' + 1) + (graph[1][3] - 'A' + 1) + (graph[1][5] - 'A' + 1) + (graph[1][7] - 'A' + 1) != 26) return false;
    if((graph[1][1] - 'A' + 1) + (graph[2][2] - 'A' + 1) + (graph[3][3] - 'A' + 1) + (graph[4][4] - 'A' + 1) != 26) return false;
    if((graph[4][4] - 'A' + 1) + (graph[3][5] - 'A' + 1) + (graph[2][6] - 'A' + 1) + (graph[1][7] - 'A' + 1) != 26) return false;

    return true;
}

void dfs(int x, int count) {
    if(count == cnt) {
        if(checkstar()){
            for(int i = 0; i < 5; i++) {
                for(int j = 0; j < 9; j++) {
                    cout << graph[i][j];
                }
                cout << endl;
            }
            exit(0);
        }
        return;
    }

    for(int i = 0; i < 12; i++) {
        if(!Select[i]) {
            Select[i] = true;
            graph[v[x].first][v[x].second] = i + 'A';
            dfs(x+1, count+1);
            Select[i] = false;
        }
    }
}

void solve() {
    dfs(0, 0);
}

void input() {
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 9; j++) {
            cin >> graph[i][j];
            if('A' <= graph[i][j] && graph[i][j] <= 'L') {
                Select[graph[i][j] - 'A'] = true;
            }
            else if(graph[i][j] == 'x') {
                v.push_back(make_pair(i, j));
                cnt++;
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

