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

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int T, N;
vector<coordinate> v;
int unf[3001];

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
    for(int i = 0; i < N-1; i++) {
        for(int j = i+1; j < N; j++) {
            int x1 = v[i].x;
            int x2 = v[j].x;

            int y1 = v[i].y;
            int y2 = v[j].y;

            int r1 = v[i].r;
            int r2 = v[j].r;

            if((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= (r1 + r2) * (r1 + r2)) {
                if(!isUnion(i, j)) {
                    Union(i, j);
                }
            }
        }
    }

    set<int> st;

    for(int i = 0; i < N; i++) {
        st.insert(Find(i));
    }

    cout << st.size() << endl;
}

void Init() {
    for(int i = 0; i < N; i++) {
        unf[i] = i;
    }
}

void input() {
    cin >> T;

    while(T--) {
        cin >> N;

        Init();
        v.clear();

        for(int i = 0; i < N; i++) {
            int x, y, R;
            cin >> x >> y >> R;
            v.push_back({x, y, R});
        }
        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
