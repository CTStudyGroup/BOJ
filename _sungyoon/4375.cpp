#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e11

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N;
ll s = 1;
int cnt = 1;

/*
 *      1을 계속 추가하며 n으로 나누어 떨어지는지 확인
 */

ll convert(string s) {
    return stol(s);
}

void solve() {
    while(true) {
        if(s % N == 0) {
            cout << cnt << endl;
            return;
        }
        else {
            s = s * 10 + 1;
            s %= N;
            cnt++;
        }
    }
}

void Init() {
    s = 1;
    cnt = 1;
}

void input() {
    while(cin >> N) {

        if(N == 0) {
            cout << 0;
            continue;
        }

        Init();
        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
