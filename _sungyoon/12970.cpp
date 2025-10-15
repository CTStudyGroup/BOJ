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

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int N, K;

void solve() {
    for (int a = 1; a < N; ++a)
    {
        int b = N - a;
        if (a * b < K)
        {
            continue;
        }

        vector<int> pos_A(b + 1);
        for (int i = 0; i < a; ++i)
        {
            int after = min(b, K);

            ++pos_A[b - after];
            K -= after;
        }

        for (int i = 0; i <= b; ++i)
        {
            for (int j = 0; j < pos_A[i]; ++j)
            {
                cout << 'A';
            }
            if (i < b)
            {
                cout << 'B';
            }
        }
        return;
    }

    cout << -1;
}

void input() {
    cin >> N >> K;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
