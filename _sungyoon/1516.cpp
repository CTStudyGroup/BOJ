#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

const int INF = 1e9;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
int inDegree[501];
int arr[501];
vector<vector<int>> v(501);
int answer[501];

void topologysort() {
    queue<pii> q;       // 노드, 시간

    for(int i = 1; i <= N; i++) {
        if(inDegree[i] == 0) {
            q.push({i, arr[i]});
            answer[i] = arr[i];
        }
    }

    while(!q.empty()) {
        int Node = q.front().first;
        int t = q.front().second;
        q.pop();

        answer[Node] = max(answer[Node], t);

        for(auto it : v[Node]) {
            if(--inDegree[it] == 0) {
                q.push({it, t + arr[it]});
            }
        }
    }
}

void solve() {
    topologysort();

    for(int i = 1; i <= N; i++) {
        cout << answer[i] << "\n";
    }
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];

        while(true) {
            int a;
            cin >> a;
            if(a == -1) break;
            inDegree[i]++;
            v[a].push_back(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
