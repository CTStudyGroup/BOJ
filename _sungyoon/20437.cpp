#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    char map[5][7];
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int T, K;
string s;
int alpha[26];
int minvalue = MAX;
int maxvalue = -MAX;

void solve() {
    int N = s.size();

    for(int i = 0; i < N; i++) {
        alpha[s[i] - 97]++;         // 알파벳 수 카운트
    }

    for(int i = 0; i < N; i++) {
        if(alpha[s[i] - 97] >= K) {
            int cnt = 0;
            for(int j = i; j < N; j++) {
                if(s[i] == s[j]) cnt++;

                if(cnt == K) {
                    minvalue = min(minvalue, j - i + 1);
                    maxvalue = max(maxvalue, j - i + 1);
                    break;
                }
            }
        }
    }

    if(maxvalue == -MAX || minvalue == MAX) {
        cout << -1 << endl;
    }
    else cout << minvalue << " " << maxvalue << endl;
}

void input() {
    cin >> T;

    while(T--) {
        minvalue = MAX;
        maxvalue = -MAX;
        memset(alpha, 0, sizeof(alpha));
        cin >> s >> K;

        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
