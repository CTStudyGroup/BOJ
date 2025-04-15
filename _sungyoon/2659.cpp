#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0};
int dy[] = {0, 0, -1, 1};
int T;
vector<int> v;
bool visited[10001];
int cnt;

int check(int a, int b, int c, int d) {
    int num1 = a * 1000 + b * 100 + c * 10 + d;
    int num2 = b * 1000 + c * 100 + d * 10 + a;
    int num3 = c * 1000 + d * 100 + a * 10 + b;
    int num4 = d * 1000 + a * 100 + b * 10 + c;

    return min({num1, num2, num3, num4});
}

void solve() {
    int end = check(v[0],  v[1], v[2], v[3]);

    for(int i = 1; i <= 9; i++) {
        for(int j = 1; j <= 9; j++) {
            for(int k = 1; k <= 9; k++) {
                for(int l = 1; l <= 9; l++) {
                    int tmp = check(i, j, k, l);
                    if(visited[tmp]) continue;
                    visited[tmp] = true;
                }
            }
        }
    }

    for(int i = 1111; i <= end; i++) {
        if(visited[i]) cnt++;
    }

    cout << cnt;
}

void input() {
    for(int i = 0; i < 4; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
