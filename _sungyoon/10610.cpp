#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e18

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
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
string s;

bool compare(int a, int b) {
    return a > b;
}

void solve() {
    int answer = 0;
    bool check = 0;
    vector<int> v;

    for(int i = 0; i < s.size(); i++) {
        int tmp = s[i] - '0';
        if(tmp == 0) check = true;
        answer += tmp;
        v.push_back(tmp);
    }

    if(check && answer % 3 == 0) {
        sort(v.begin(), v.end(), compare);
        for(auto it : v) {
            cout << it;
        }
    }
    else cout << -1;
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

