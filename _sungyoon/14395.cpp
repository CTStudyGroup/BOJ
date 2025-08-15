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

struct nutrition {
    int p;
    int f;
    int s;
    int v;
    int cost;
};

int dx[] = {0 ,0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {0, -1, 0, 1, 0, -1, 1, -1, 1};
ll s, t;
set<ll> st;

bool check(int a) {
    if(a < 0 || a > MAX) return false;

    if(st.find(a) != st.end()) {
        return false;
    }
    return true;
}

void bfs() {
    queue<tuple<ll, string>> q;
    q.push({s, ""});
    st.insert(s);

    while(!q.empty()) {
        ll x = get<0>(q.front());
        string sol = get<1>(q.front());
        q.pop();

        if(x == t) {
            cout << sol;
            exit(0);
        }

        for(int i = 0; i < 4; i++) {
            if(i == 0) {
                ll stand = x * x;
                if(check(stand)) {
                    q.push({stand, sol + '*'});
                    st.insert(stand);
                }
            }
            else if(i == 1) {
                ll stand = x + x;
                if(check(stand)) {
                    q.push({stand, sol + '+'});
                    st.insert(stand);
                }
            }
            else if(i == 2) {
                ll stand = x - x;
                if(check(stand)) {
                    q.push({stand, sol + '-'});
                    st.insert(stand);
                }
            }
            else {
                ll stand = x / x;
                if(check(stand)) {
                    q.push({stand, sol + '/'});
                    st.insert(stand);
                }
            }
        }
    }
}

void solve() {
    if(s == t) {
        cout << 0;
        return;
    }

    bfs();

    cout << -1;
}

void input() {
    cin >> s >> t;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

