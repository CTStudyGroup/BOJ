#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N;

void hanoi(int start, int mid, int end, int n) {
    if(n == 1) {
        cout << start << " " << end << endl;
        return;
    }

    hanoi(start, end, mid, n-1);
    cout << start << " " << end << endl;
    hanoi(mid, start, end, n-1);
}

void solve() {
    cout << (int)pow(2, N) - 1 << endl;

    hanoi(1, 2, 3, N);
}

void input() {
    cin >> N;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
