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

int dx[] = {0 ,0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {0, -1, 0, 1, 0, -1, 1, -1, 1};
int N, K;
queue<int> q[21];
int arr[300001];

void solve() {
    ll cnt = 0;

    for(int i = 1;  i <= N; i++) {
        while(!q[arr[i]].empty() && i - q[arr[i]].front() > K) q[arr[i]].pop();
        cnt += q[arr[i]].size();
        q[arr[i]].push(i);
    }

    cout << cnt;
}

void input() {
    cin >> N >> K;

    for(int i = 1; i <= N; i++) {
        string s;
        cin >> s;
        arr[i] = s.length();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

