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
string s;
unordered_map<char, int> um;

void solve() {
    int start = 0, end = 0;
    int answer = 0;
    um[s[0]]++;

    while(start <= end && end < s.size()) {
        if(um.size() > N) {
            um[s[start]]--;
            if(um[s[start]] == 0) um.erase(s[start]);
            start++;
        }
        answer = max(answer, end - start+1);

        end++;
        um[s[end]]++;
    }

    cout << answer;
}

void input() {
    cin >> N >> s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

