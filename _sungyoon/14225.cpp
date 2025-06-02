#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e11

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N;
int arr[21];
bool check[2000001];

void solve() {
    for(int i = 1; i < (1 << N); i++) {
        int sum = 0;
        for(int j = 0; j < N; j++) {
            if(i & (1 << j)) {
                sum += arr[j];
            }
        }
        check[sum] = true;
    }

    for(int i = 1; i <= 20000000; i++) {
        if(!check[i]) {
            cout << i;
            return;
        }
    }
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
