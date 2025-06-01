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
int N, K, P, X, result;
bool check[10][7] = {{true, true, true, false, true, true, true},
                     {false, false, true, false, false, true, false},
                     {true, false, true, true, true, false, true},
                     {true, false, true, true, false, true, true},
                     {false, true, true, true, false, true, false},
                     {true, true, false, true, false, true, true},
                     {true, true, false, true, true, true, true},
                     {true, false, true, false, false, true, false},
                     {true, true, true, true, true, true, true},
                     {true, true, true, true, false, true, true}};
vector<int> v;

/*
 * N -> N 이하 층
 * K -> K자리 수 디스플레이
 * P -> 최대 P개 반전
 * X -> 실제 멈춰있는 층
 */

int diff(int x, int y) {
    int cnt = 0;

    for(int i = 0; i < 7; i++) {
        if(check[x][i] != check[y][i]) {
            cnt++;
        }
    }
    return cnt;
}

void bt(int idx, int cnt,vector<int> &tmp) {
    if(cnt > P) return;

    if(idx == K) {
        int num = 0;

        for(auto it : tmp) {
            num = num * 10 + it;
        }

        if(num >= 1 && num <= N && num != X) {
            result++;
        }
        return;
    }

    int stand = v[idx];

    for(int i = 0; i < 10; i++) {
        int df = diff(stand, i);
        tmp[idx] = i;
        bt(idx + 1, cnt + df, tmp);
    }
}

void solve() {
    v.resize(K);

    int x = X;

    for(int i = K - 1; i >= 0; i--) {
        int tmp = x % 10;
        v[i] = tmp;
        x /= 10;
    }

    vector<int> tmpv = v;

    bt(0, 0, tmpv);

    cout << result;
}

void input() {
    cin >> N >> K >> P >> X;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
