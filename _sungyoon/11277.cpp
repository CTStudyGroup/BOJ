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
int N, M;
vector<pii> v;
int arr[21];

bool check() {
    for(int i = 0; i < M; i++) {
        int a = (v[i].first > 0) ? arr[v[i].first] : !arr[v[i].first * -1];
        int b = (v[i].second > 0) ? arr[v[i].second] : !arr[v[i].second * -1];

        if(!(a || b)) {
            return false;
        }
    }

    return true;
}

void solve() {
    for(int i = 0; i < (1 << N); i++) {
        for(int j = 1; j <= N; j++) {
            arr[j] = ((i >> (j-1)) & 1);
        }

        if(check()) {
            cout << 1;
            return;
        }
    }
    cout << 0;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

