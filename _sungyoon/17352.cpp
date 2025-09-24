// baekjoon 17835
#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define INF int(1e9)

int dx[9] = {-1, 1, 0, 0, -1, -1, 1, 1, 0};
int dy[9] = {0, 0, -1, 1, -1, 1, -1, 1, 0};
int uni[300001];
int N;

int Find(int x) {
    if(x == uni[x]) return x;
    else return uni[x] = Find(uni[x]);
}

void Union(int x, int y) {
    x = Find(x);
    y = Find(y);

    if(x < y) uni[y] = x;
    else uni[x] = y;
}

bool isUnion(int x, int y) {
    x = Find(x);
    y = Find(y);

    if(x == y) return true;
    else return false;
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        uni[i] = i;
    }

    for(int i = 0; i < N-2; i++) {
        int a, b;
        cin >> a >> b;
        Union(a, b);
    }

    for(int i = 2; i <= N; i++) {
        if(!isUnion(1, i)) {
            cout << "1 " << i;
            return;
        }
    }
}

void solve() {
    input();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    solve();
}

