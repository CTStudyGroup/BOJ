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

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N, M;
int unf[100001];
int arr[100001];

int Find(int a) {
    if(a == unf[a]) return a;
    return unf[a] = Find(unf[a]);
}

void Union(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(a > b) unf[a] = b;
    else unf[b] = a;
}

bool isUnion(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(a == b) return true;
    else return false;
}

void Init() {
    for(int i = 1; i <= N; i++) {
        unf[i] = i;
    }
}

void solve() {
    int cnt = 0;

    for(int i = 1; i < N; i++) {
        if(!isUnion(arr[i-1], arr[i])) {
            cnt++;
        }
    }

    cout << cnt;
}

void input() {
    cin >> N >> M;

    Init();

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;

        if(!isUnion(a, b)) {
            Union(a, b);
        }
    }

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

