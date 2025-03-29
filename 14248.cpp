#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {0,-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0,0, 0, -1, 1, -1, 1, -1, 1};
int N, S, result;
int arr[100001];
bool visited[100001];

void bfs() {
    queue<pii> q;
    q.push(make_pair(S, 0));
    visited[S] = true;

    while(!q.empty()) {
        int xx = q.front().first;
        int cnt = q.front().second;
        q.pop();

        int dist = arr[xx];
        int left = xx + dist;
        int right = xx - dist;

        if(right >= 1 && right <= N) {
            if(!visited[right]) {
                q.push(make_pair(right, cnt + 1));
                visited[right] = true;
            }
        }
        if(left >= 1 && left <= N) {
            if(!visited[left]) {
                q.push(make_pair(left, cnt+1));
                visited[left] = true;
            }
        }
    }
}

void solve() {
    bfs();

    for(int i = 1; i <= N; i++) {
        if(visited[i]) result++;
    }

    cout << result;
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    cin >> S;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

