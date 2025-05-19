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
int N, K;
ll lens;

void solve() {
    int result = -1;

    for(int i = 1; i <= N; i++) {
        string tmp = to_string(i);

        ll tmplens = tmp.size();
        lens += tmplens;

        if(lens >= K) {
            int num = lens - tmp.size();
            result = tmp[K-num-1] - '0';
            break;
        }
    }

    cout << result;
}

void input() {
    cin >> N >> K;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
