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

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int N;
vector<char> v;

void solve() {
    sort(v.begin(), v.end());

    do {
        for(auto it = v.begin(); it != v.end(); it++) {
            cout << *it;
        }
        cout << endl;
    } while(next_permutation(v.begin(), v.end()));
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;

        for(int j = 0; j < s.size(); j++) {
            v.push_back(s[j]);
        }

        solve();
        v.clear();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

