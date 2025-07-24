#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int T, K;
bool isPrime[1300000];

void Init() {
    for(int i = 2; i <= 1299709; i++) {
        for(int j = i + i; j <= 1299709; j += i) {
            if(!isPrime[j]) {
                isPrime[j] = true;
            }
        }
    }
}

void solve() {
    if(!isPrime[K]) {       // 소수인 경우
        cout << 0 << endl;
        return;
    }

    int start = 2;
    int end = K;

    for(int i = 2; i < K; i++) {
        if(!isPrime[i]) {
            start = max(start, i);
        }
    }

    for(int i = K+1; i <= 1299709; i++) {
        if(!isPrime[i]) {
            end = i;
            break;
        }
    }

    cout << end - start << endl;
}

void input() {
    cin >> T;

    Init();

    while(T--) {
        cin >> K;

        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
