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
string s;
int zero, one;

/*
 *   사전순으로 가장 앞에 위치해야 하기 때문에 0은 앞에 위치하기
 *   1은 뒤에 위치하기
 */

void solve() {
    for(int i = 0; i < s.size(); i++) {
        if(s[i] - '0' == 0) zero++;
        else one++;
    }

    zero = zero / 2;
    one = one / 2;

    int tmp = 0;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '1') {
            tmp++;
            s[i] = -1;
        }

        if(one == tmp) break;
    }

    tmp = 0;

    for(int i = s.size(); i >= 0; i--) {
        if(s[i] == '0') {
            tmp++;
            s[i] = -1;
        }

        if(zero == tmp) break;
    }

    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '0' || s[i] == '1') {
            cout << s[i];
        }
    }
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
