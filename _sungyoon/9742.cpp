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
int N, sz, cnt;
string s;
char arr[11];
bool visited[11];
bool flag;

void bt(int x) {
    if(x == sz) {
        cnt++;
        if(cnt == N) {
            flag = true;
            cout << s << " " << N << " = ";
            for(int i = 0; i < sz; i++) {
                cout << (char)arr[i];
            }
            cout << endl;
        }
        return;
    }

    for(int i = 0; i < sz; i++) {
        if(!visited[i]) {
            visited[i] = true;
            arr[x] = s[i];
            bt(x+1);
            visited[i] = false;
        }
    }
}

void solve() {
    flag = false;
    sz = s.size();
    cnt = 0;
    bt(0);

    if(!flag) {
        cout << s << " " << N << " = " << "No permutation" << endl;
    }
}

void input() {
    while(cin >> s >> N) {
        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

