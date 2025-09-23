// baekjoon 4889
#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1025

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1 ,1};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    int cnt = 1;
    string s;

    while(true) {
        cin >> s;
        if(s[0] == '-') break;

        int res = 0;
        stack<char> st;

        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '{') {
                st.push('{');
            }
            else {
                if(!st.empty()) st.pop();
                else {
                    st.push('{');
                    res++;
                }
            }
        }
        res += int(st.size() / 2);

        cout << cnt << ". " << res << endl;
        cnt++;
    }
}
