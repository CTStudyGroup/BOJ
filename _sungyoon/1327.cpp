#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, K;
vector<int> v;
map<string, int> m;
string stand = "";

bool check(string s) {
    string tmpnum = "123456789";

    for(int i = 0; i < N; i++) {
        if(s[i] != tmpnum[i]) return false;
    }
    return true;
}

void bfs(string s) {
    queue<pair<string, int>> q;
    q.push(make_pair(s, 0));
    m[s] = 1;

    while(!q.empty()) {
        string st = q.front().first;
        int cnt = q.front().second;
        q.pop();

        if(check(st)) {
            cout << cnt;
            exit(0);
        }

        for(int i = 0; i <= N-K; i++) {
            string num = st;
            queue<char> dq;

            for(int j = (i + K)-1; j >= i; j--) {
                dq.push(st[j]);
            }

            for(int j = i; j < i + K; j++) {
                num[j] = dq.front();
                dq.pop();
            }

            if(m.find(num) == m.end())  {
                q.push(make_pair(num, cnt+1));
                m[num] = 1;
            }
        }
    }
}

void solve() {
    bfs(stand);

    cout << -1;
}

void input() {
    cin >> N >> K;

    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        stand += s;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
