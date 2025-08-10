#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    string s;
    vector<int> v;
};

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int N, Q;
bool tree[1100000];

void solve() {

}

void input() {
    cin >> N >> Q;

    for(int i = 0; i < Q; i++) {
        int a;
        cin >> a;
        int tmp = a;
        int res = 0;
        bool flag = false;
        while(tmp != 1) {
            if(tree[tmp]) {
                flag = true;
                res = tmp;
            }
            tmp /= 2;
        }
        if(flag) {
            cout << res << endl;
        }
        else {
            tree[a] = true;
            cout << 0 << endl;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
