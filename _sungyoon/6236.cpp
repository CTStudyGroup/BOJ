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
int N, M;
vector<int> v;

void solve() {
    ll start = 0;
    ll end = int(1e9);

    while(start + 1 < end) {
        ll mid = (start + end) / 2;

        bool visited = false;
        int cnt = 0;
        ll money = 0;
        for(int i = 0; i < v.size(); i++) {
            if(v[i] > mid) {
                visited = true;
                break;
            }

            if(money < v[i]) {
                cnt++;
                money = mid;
            }
            money -= v[i];
        }

        if(!visited && cnt <= M) {
            end = mid;
        }
        else start = mid;
    }

    cout << start + 1;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
