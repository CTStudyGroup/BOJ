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
int N, M, K;
int friendCost[10001];
int unf[10001];

int Find(int a) {
    if(a == unf[a]) return a;
    return unf[a] = Find(unf[a]);
}

void Union(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(friendCost[a] > friendCost[b]) {
        unf[a] = b;
    }
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
    set<int> st;

    for(int i = 1; i <= N; i++) {
        st.insert(Find(unf[i]));
    }

    int cost = 0;

    for(auto it : st) {
        cost += friendCost[it];
    }

    if(cost <= K) {
        cout << cost;
    }
    else cout << "Oh no";
}

void input() {
    cin >> N >> M >> K;

    Init();

    for(int i = 1; i <= N; i++) {
        cin >> friendCost[i];
    }

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        Union(a, b);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();

    return 0;
}
