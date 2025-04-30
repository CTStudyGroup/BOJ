#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int R, C, result;
vector<string> v;

bool check(int r) {
    set<string> st;

    for(int i = 0; i < C; i++) {
        string tmp;
        for(int j = r; j < R; j++) {
            tmp += v[j][i];
        }
        if(st.count(tmp)) return false;
        st.insert(tmp);
    }
    return true;
}

void solve() {
    int tp = 0;
    int bottom = R-1;

    while(tp <= bottom) {
        int mid = (tp + bottom) / 2;

        if(check(mid)) {        // 중복된 것이 없을 경우
            result = mid;
            tp = mid+1;
        }
        else bottom = mid-1;
    }

    cout << result;
}

void input() {
    cin >> R >> C;

    for(int i = 0; i < R; i++) {
        string s;
        cin >> s;
        v.push_back(s);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
