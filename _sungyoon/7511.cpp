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

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int T, N, K, M;
int test = 1;
int unf[100000];

int Find(int a) {
    if(a == unf[a]) return a;
    return a = Find(unf[a]);
}

void Union(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(a > b) unf[b] = a;
    else unf[a] = b;
}

bool isUnion(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(a == b) return true;
    else return false;
}

void Init() {
    for(int i = 0; i < N; i++) {
        unf[i] = i;
    }
}

void input() {
    cin >> T;

    while(T--) {
        cin >> N >> K;

        Init();

        for(int i = 0; i < K; i++) {
            int a, b;
            cin >> a >> b;
            Union(a, b);
        }

        cin >> M;

        cout << "Scenario " << test << ":" << endl;

        for(int i = 0; i < M; i++) {
            int u, v;
            cin >> u >> v;
            if(isUnion(u, v)) {
                cout << 1 << endl;
            }
            else cout << 0 << endl;
        }
        cout << endl;

        test++;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
