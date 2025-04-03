#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define Endl "\n"
#define MAX 1e9

int dx[] = {0, -1 , 1, 0, -1, -1, 1, 1};
int dy[] = {-1, 0, 0, 1, -1, 1, -1, 1};
string X;
string arr[10];
string result[10];
int sol = MAX;
bool visited[10];

int convert(string a) {
    if(a[0] == '0') {
        return 0;
    }

    return stoi(a);
}

void bt(int x) {
    if(x == X.size()) {
        string tmp = "";
        for(int i = 0; i < X.size(); i++) {
            tmp += result[i];
        }
        int res = convert(tmp);
        if(res > convert(X)) {
            sol = min(res, sol);
        }
        return;
    }

    for(int i = 0; i < X.size(); i++) {
        if(!visited[i]) {
            result[x] = arr[i];
            visited[i] = true;
            bt(x+1);
            visited[i] = false;
        }
    }
}

void solve() {
    bt(0);

    if(sol == MAX) {
        cout << 0;
    }
    else {
        cout << sol;
    }
}

void input() {
    cin >> X;

    for(int i = 0; i < X.size(); i++) {
        arr[i] = X[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
