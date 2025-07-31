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

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int N;
vector<vector<int>> v(100001);
bool visited[100001];
int order[100001];
int bfs_order[100001];

bool cmp(int a, int b) {
    return order[a] < order[b];
}

void bfs(int a) {
    queue<int> q;
    q.push(a);
    visited[a] = true;
    int idx = a;

    while(!q.empty()) {
        int x = q.front();
        q.pop();

        bfs_order[x] = idx++;

        for(auto it : v[x]) {
            if(!visited[it]) {
                q.push(it);
                visited[it] = true;
            }
        }
    }
}

void solve() {
    bfs(1);

    bool isflag = false;
    for(int i = 1; i <= N; i++) {
        if(order[i] != bfs_order[i]) {
            isflag = true;
            break;
        }
    }


    if(!isflag) {
        cout << 1;
    }
    else cout << 0;
}

void input() {
    cin >> N;

    for(int i = 0; i < N-1; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    for(int i = 1; i <= N; i++) {
        int a;
        cin >> a;
        order[a] = i;
    }

    for(int i = 1; i <= N; i++) {
        sort(v[i].begin(), v[i].end(), cmp);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
