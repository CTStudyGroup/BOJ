#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define Endl "\n"
#define MAX 1e9

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N;
int arr[] = {0, 1, 2};
int result[10];
int res;

int convert(string a) {
    if(a[0] == '0') {
        return 0;
    }
    return stoi(a);
}

void dfs(int x) {
    if(x == N) {
        string s;
        for(int i = 0; i < N; i++) {
            s += to_string(result[i]);
        }
        int tmp = convert(s);
        if(tmp == 0) {
            return;
        }
        else if(tmp % 3 == 0) {
            res++;
        }
        return;
    }

    for(int i = 0; i < 3; i++) {
        result[x] = arr[i];
        dfs(x+1);
    }
}

void solve() {
    dfs(0);
    cout << res;
}

void input() {
    cin >> N;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

