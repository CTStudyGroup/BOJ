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
int N, M;
string arrs[11];
bool visited[11];
vector<vector<int>> v(11);
bool flag;
int tmpcnt1 = MAX;
int tmpcnt2 = MAX;
int tmpcount;

void bt(int x, int cnt, int num) {
    if(cnt == num) {
        set<int> st;
        for(int i = 1; i <= N; i++) {
            if(visited[i]) {
                for(auto it : v[i]) {
                    st.insert(it);
                }
            }
        }
        if(st.size() == M) {
            flag = true;
            tmpcnt1 = min(tmpcnt1, num);
        }
        else {
            if(st.size() > tmpcount) {
                tmpcount = st.size();
                tmpcnt2 = num;
            }
            else if(st.size() == tmpcount) {
                tmpcnt2 = min(tmpcnt2, num);
            }
        }
        return;
    }

    for(int i = x; i <= N; i++) {
        if(!visited[i]) {
            visited[i] = true;
            bt(i+1, cnt+1, num);
            visited[i] = false;
        }
    }
}

void solve() {
    for(int i = 1; i <= N; i++) {
        bt(1, 0, i);
    }

    if(flag) {
        cout << tmpcnt1;
    }
    else {
        if(!tmpcount) {
            cout << -1;
        }
        else cout << tmpcnt2;
    }
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        string a, b;
        cin >> a >> b;
        arrs[i+1] = a;

        for(int j = 0; j < b.size(); j++) {
            if(b[j] == 'Y') {
                v[i+1].push_back(j+1);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
