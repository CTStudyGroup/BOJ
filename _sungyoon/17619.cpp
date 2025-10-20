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
vector<tuple<int, int, int, int>> v;
int unf[100001];

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

void solve() {
    sort(v.begin(), v.end());

    int startx = get<0>(v[0]);
    int endx = get<1>(v[0]);
    int idx = get<3>(v[0]);
    for(int i = 1; i < N; i++) {
        int nx = get<0>(v[i]);
        int ny = get<1>(v[i]);
        int element = get<3>(v[i]);

        if(endx >= nx) {
            Union(get<3>(v[i-1]), get<3>(v[i]));
            endx = max(endx, ny);
        }
        else {
            startx = nx;
            endx = ny;
        }
    }

    for(int i = 0; i < M; i++) {
        int x1, x2;
        cin >> x1 >> x2;

        if(isUnion(x1, x2)) {
            cout << 1 << endl;
        }
        else cout << 0 << endl;
    }
}

void Init() {
    for(int i = 1; i <= N; i++) {
        unf[i] = i;
    }
}

void input() {
    cin >> N >> M;

    Init();

    for(int i = 1; i <= N; i++) {
        int x1, x2, y;
        cin >> x1 >> x2 >> y;
        v.push_back({x1, x2, y, i});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

