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

int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
vector<int> v;

void Print() {
    for(auto it : v) {
        cout << it << endl;
    }
}

void solve() {
    int bits = (1 << 26) - 1;

    for(int i = 0; i < M; i++) {
        int a;
        char b;
        int cnt = 0;
        cin >> a >> b;

        if(a == 1) {        // 단어를 잊음
            bits &= ~(1 << (b - 'a'));
        }
        else {
            bits |= (1 << (b - 'a'));
        }

        for(int j = 0; j < N; j++) {
            if((v[j] & bits) == v[j]) {
                cnt++;
            }
        }

        cout << cnt << endl;
    }
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        string s;
        int a = 0;
        cin >> s;

        for(int j = 0; j < s.size(); j++) {
            a |= (1 << (s[j] - 'a'));
        }

        v.push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

