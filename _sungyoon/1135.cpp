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

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
vector<vector<int>> v(51);

bool compare(int a, int b) {
    return a > b;
}

int dfs(int Node) {
    vector<int> arr;
    int time = 1;
    int max_time = 0;

    for(auto it : v[Node]) {
        int t = dfs(it);
        arr.push_back(t);
    }

    sort(arr.begin(), arr.end(), compare);

    for(auto it : arr) {
        max_time = max(max_time, time + it);
        time++;
    }

    return max_time;
}

void solve() {
    cout << dfs(0);
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;

        if(a == -1) continue;

        v[a].push_back(i);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

