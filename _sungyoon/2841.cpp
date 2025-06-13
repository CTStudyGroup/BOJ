#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e8

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, P;
stack<int> st[7];
int cnt;

void solve() {

}

void input() {
    cin >> N >> P;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;

        if(st[a].empty()) {
            st[a].push(b);
            cnt++;
        }
        else if(st[a].top() < b) {
            st[a].push(b);
            cnt++;
        }
        else if(st[a].top() > b)  {
            while(st[a].top() > b) {
                st[a].pop();
                cnt++;
                if(st[a].empty()) {
                    st[a].push(b);
                    cnt++;
                }
            }
        }

        if(st[a].top() < b) {
            st[a].push(b);
            cnt++;
        }
    }

    cout << cnt;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
