#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

struct FISH {
    int x;
    int y;
    int Dir;
    bool live;
};

//int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int N, M;
int graph[101][101];
int unf[101];
map<int, vector<int>> m;
vector<int> v;

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

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            if(i == j) continue;
            graph[i][j] = MAX;
        }
    }
}

void solve() {
    for(int k = 1; k <= N; k++) {
        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= N; j++) {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }

    for(int i = 1; i <= N; i++) {
        int parent = Find(i);
        m[parent].push_back(i);
    }

    for(auto it : m) {
        int dist = MAX;
        int person = 0;

        for(auto iter : it.second) {
            int tmpdist = 0;

            for(auto iterate : it.second) {
                if(iter == iterate) continue;
                tmpdist = max(tmpdist, graph[iter][iterate]);
            }

            if(tmpdist < dist) {
                dist = tmpdist;
                person = iter;
            }
        }
        v.push_back(person);
    }

    sort(v.begin(), v.end());

    cout << v.size() << endl;

    for(auto it : v) {
        cout << it << endl;
    }
}

void input() {
    cin >> N >> M;

    Init();

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
        Union(a, b);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
