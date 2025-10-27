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

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {1, 0};
int dy[] = {0, 1};
int N;
int arr[250001];
int ans;
vector<ll> v;

void solve() {
    if(ans == 0) {
        ans = ans + N / 2;
    }
    else {
        for (int i = 0; i < v.size(); i++){
            if (i == v.size() - 1){
                num = (N - v[i] + v[0]) / 2;
                ans = ans + num;
            }
            else {
                num = (v[i+1] - v[i]) / 2;
                ans = ans + num;
            }
            num = 0;
        }    
    }

    cout << ans;
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
        ans = ans + arr[i];
        if(arr[i]) {
            v.push_back(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

