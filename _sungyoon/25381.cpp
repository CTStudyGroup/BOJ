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
string s;

void solve() {
    int cnt = 0;
    deque<int> dq;

    for(int i = 0; i < s.size(); i++) {
        if(s[i] == 'B') {
            dq.push_back(i);
        }
    }

    for(int i = 0; i < s.size(); i++) {        // C 제거
        if(s[i] == 'C') {
            if(dq.size() != 0 && dq.front() < i) {
                dq.pop_front();
                cnt++;
            }
        }
    }

    for(int i = s.size()-1; i >= 0; i--) {
        if(s[i] == 'A') {
            if(dq.size() != 0 && dq.back() > i) {
                dq.pop_back();
                cnt++;
            }
        }
    }

    cout << cnt;
}

void input() {
    cin >> s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
