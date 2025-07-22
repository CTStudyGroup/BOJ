#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int a, b, c;
int dp[51][51][51];

int solve(int x, int y, int z) {
    if(x <= 0 || y <= 0 || z <= 0) {
        return 1;
    }
    if(x > 20 || y > 20 || z > 20) {
        return solve(20, 20, 20);
    }

    int &ret = dp[x][y][z];
    if(ret != -1) return dp[x][y][z];

    if(x < y && y < z) {
        ret = solve(x, y, z-1) + solve(x, y-1, z-1) - solve(x, y-1, z);
    }
    else {
        ret = solve(x-1, y, z) + solve(x-1, y-1, z) + solve(x-1, y, z-1) - solve(x-1, y-1, z-1);
    }
    return ret;
}

void input() {
    memset(dp, -1, sizeof(dp));
    
    while(true) {
        cin >> a >> b >> c;

        if(a == -1 && b == -1 && c == -1) {
            break;
        }

        cout << "w(" << a << ", " << b << ", " << c << ") " << "= " << solve(a, b, c) << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
