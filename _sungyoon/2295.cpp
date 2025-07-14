#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0,1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int T;
string s;

void solve() {
    string tmp = "";

    list<char> li(tmp.begin(), tmp.end());

    auto idx = li.end();

    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '<') {
            if(idx != li.begin()) {
                idx--;
            }
        }
        else if(s[i] == '>') {
            if(idx != li.end()) {
                idx++;
            }
        }
        else if(s[i] == '-') {
            if(idx != li.begin()) {
                idx--;
                idx = li.erase(idx);
            }
        }
        else {
            li.insert(idx, s[i]);
        }
    }

    for(auto it : li) {
        cout << it;
    }
    cout << endl;
}

void input() {
    cin >> T;

    while(T--) {
        cin >> s;

        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
