#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

const int INF = 1e9;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int T, n, m;
vector<int> a, b;
vector<int> piz1, piz2;

void Print() {
    for(auto it : piz1) {
        cout << it << " ";
    }
    cout << endl;

    for(auto it : piz2) {
        cout << it << " ";
    }
    cout << endl;
}

void solve() {
    piz1.push_back(0);          // 선택하지 않은 경우
    piz2.push_back(0);          // 선택하지 않은 경우

    for(int i = 0; i < m; i++) {
        int pizza = 0;
        for(int j = i; j < i + m - 1; j++) {
            pizza += a[j % m];
            piz1.push_back(pizza);
        }
    }

    int tmp = 0;
    for(int i = 0; i < m; i++) {
        tmp += a[i];
    }
    piz1.push_back(tmp);

    for(int i = 0; i < n; i++) {
        int tmp = 0;
        for(int j = i; j < i + n - 1; j++) {
            tmp += b[j % n];
            piz2.push_back(tmp);
        }
    }

    tmp = 0;
    for(int i = 0; i < n; i++) {
        tmp += b[i];
    }

    piz2.push_back(tmp);

    sort(piz1.begin(), piz1.end());
    sort(piz2.begin(), piz2.end());

    int answer = 0;     // 경우의 수

    for(int i = 0; i < piz1.size(); i++) {
        int val = T - piz1[i];

        if(val < 0) continue;
        else {
            int idx1 = lower_bound(piz2.begin(), piz2.end(), val) - piz2.begin();
            int idx2 = upper_bound(piz2.begin(), piz2.end(), val) - piz2.begin();

            answer += idx2 - idx1;
        }
    }

    cout << answer << endl;
}

void input() {
    cin >> T >> m >> n;

    for(int i = 0; i < m; i++) {
        int t;
        cin >> t;
        a.push_back(t);
    }

    for(int i = 0; i < n; i++) {
        int t;
        cin >> t;
        b.push_back(t);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
