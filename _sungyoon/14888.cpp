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

int dx[] = {0 ,0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {0, -1, 0, 1, 0, -1, 1, -1, 1};
int N, pluses, minuses, mult, divi;
vector<int> v;
int arr[4];
int maxval = -MAX;
int minval = MAX;

void dfs(int cnt, int val) {
    if(cnt == N-1) {
        maxval = max(val, maxval);
        minval = min(val, minval);
        return;
    }

    if(pluses > 0) {
        pluses--;
        dfs(cnt+1, val + v[cnt+1]);
        pluses++;
    }

    if(minuses > 0) {
        minuses--;
        dfs(cnt+1, val - v[cnt+1]);
        minuses++;
    }

    if(mult > 0) {
        mult--;
        dfs(cnt+1, val * v[cnt+1]);
        mult++;
    }

    if(divi > 0) {
        divi--;
        dfs(cnt+1, val / v[cnt+1]);
        divi++;
    }
}

void solve() {
    dfs(0, v[0]);

    cout << maxval << endl << minval;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }

    cin >> pluses >> minuses >> mult >> divi;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

