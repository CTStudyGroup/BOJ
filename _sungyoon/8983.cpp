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
int M, N, L;
vector<int> arr;
vector<pii> animal;

void solve() {
    sort(arr.begin(), arr.end());
    int cnt = 0;

    for(int i = 0; i < N; i++) {
        ll x = animal[i].first;
        ll y = animal[i].second;

        int idx = lower_bound(arr.begin(), arr.end(), x) - arr.begin();

        if(abs(arr[idx] - x) + y <= L) {
            cnt++;
            continue;
        }

        if(idx - 1 >= 0) {
            if(abs(arr[idx-1] - x) + y <= L) {
                cnt++;
            }
        }
    }

    cout << cnt;
}

void input() {
    cin >> M >> N >> L;

    arr.assign(M, 0);

    for(auto &it : arr) {
        cin >> it;
    }

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        animal.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

