#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int result;
string s;

int getdigit(char a) {
    int res = a - '0';

    return res;
}

void solve() {
    stack<int> st;

    for(int i = 0; i < s.length(); i++) {
        char stand = s[i];

        if(stand == '(') {
            st.push(-1);
        }
        else if(stand == ')') {
            int tmp = 0;
            while(st.top() != -1) {
                int pre = st.top();
                tmp += pre;
                st.pop();
            }
            st.pop();
            st.push(tmp);
        }
        else if(stand == 'H') {
            st.push(1);
        }
        else if(stand == 'C') {
            st.push(12);
        }
        else if(stand == 'O') {
            st.push(16);
        }
        else {
            int temp = st.top();
            st.pop();
            temp *= getdigit(stand);
            st.push(temp);
        }
    }

    while(!st.empty()) {
        int tp = st.top();
        result += tp;
        st.pop();
    }

    cout << result;
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

