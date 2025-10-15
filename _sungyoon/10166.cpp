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

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 0, 1, -1};
int dy[] = {0, 1, -1, 0, 0};
int D1, D2;
bool check[2001][2001];

void solve() {
    int answer = 1;

    for(int i = D1; i <= D2; i++) {
        for(int j = 1; j < i; j++) {
            int mod = gcd(i, j);

            int up = i / mod;
            int down = j / mod;

            if(!check[up][down]) {
                answer++;
                check[up][down] = true;
            }
        }
    }

    cout << answer;
}

void input() {
    cin >> D1 >> D2;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

