#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N;
int result;

void solve() {
    deque<tuple<int, int, int>> dq;

    for(int i = 0; i < N; i++) {
        int a, b, c;
        cin >> a;
        if(a == 1) {
            cin >> b >> c;
            dq.push_front(make_tuple(a, b, --c));
            if(get<2>(dq.front()) == 0) {
                result += get<1>(dq.front());
                dq.pop_front();
            }
        }
        else {
            int miniute = get<2>(dq.front());
            get<2>(dq.front())--;
            if(get<2>(dq.front()) == 0) {
                result += get<1>(dq.front());
                dq.pop_front();
            }
        }
    }

    cout << result;
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
