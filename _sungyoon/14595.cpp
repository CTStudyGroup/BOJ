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
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {1, 0};
int dy[] = {0, 1};
int N, M, lo;
int unf[1000001];
bool visited[1000001];
vector<pii> v;

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
    sort(v.begin(), v.end());

    for(auto it : v) {
        int a = it.first;
        int b = it.second;

        a = max(lo, a);

        for(int i = lo; i <= b; i++) {
            Union(a, i);
        }

        lo = max(lo, b);
    }

    int answer = 0;

    for(int i = 1; i <= N; i++) {
        int a = Find(i);

        if(!visited[a]) {
            visited[a] = true;
            answer++;
        }
    }

    cout << answer;
}

void input() {
    cin >> N >> M;

    Init();

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

