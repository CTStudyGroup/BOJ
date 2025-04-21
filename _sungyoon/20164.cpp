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
string s;
int minCnt = MAX, maxCnt;

void bt(string a, int cnt) {
    for(int i = 0; i < a.size(); i++) {
        int stand = a[i] - '0';

        if(stand % 2 != 0) {
            cnt++;
        }
    }

    if(a.length() == 1) {
        int tmp = stoi(a);

        maxCnt = max(maxCnt, cnt);
        minCnt = min(minCnt, cnt);
        return;
    }
    else if(a.length() == 2) {
        int tmpa = a[0] - '0';
        int tmpb = a[1] - '0';

        int tmpnum = tmpa + tmpb;

        bt(to_string(tmpnum), cnt);
    }
    else {
        for(int i = 0; i < a.length() - 2; i++) {
            for(int j = i+1; j < a.length()-1; j++) {
                string s1 = a.substr(0, i + 1);
                string s2 = a.substr(i + 1, j - i);
                string s3 = a.substr(j + 1);

                int a1 = stoi(s1);
                int a2 = stoi(s2);
                int a3 = stoi(s3);

                bt(to_string(a1 + a2 + a3), cnt);
            }
        }
    }
}

void solve() {
    bt(s, 0);

    cout << minCnt << " " << maxCnt;
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
