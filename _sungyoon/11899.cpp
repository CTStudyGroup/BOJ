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

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
string s;

void solve() {
    stack<char> st;

    for(int i = 0; i < s.size(); i++) {
        char stand = s[i];

        if(st.empty()) {
            st.push(stand);
            continue;
        }

        if(st.top() == '(' && stand == ')') {
            st.pop();
            continue;
        }

        st.push(stand);
    }

    cout << st.size();
}

void input() {
    cin >> s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
