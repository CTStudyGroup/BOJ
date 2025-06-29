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

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int K;      // 트리의 높이
int arr[1025];
vector<vector<int>> v(11);

void dfs(int start, int end, int level) {
    int mid = (start + end) / 2;
    v[level].push_back(arr[mid]);
    if(level == K) return;

    dfs(start, mid-1, level+1);
    dfs(mid+1, end, level+1);
}

void solve() {
    int start = 0;
    int end = (1 << K) - 2;

    dfs(start, end, 1);

    for(int i = 1; i <= K; i++) {
        for(int j = 0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}

void input() {
    cin >> K;

    for(int i = 0; i < (1 << K)-1; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
