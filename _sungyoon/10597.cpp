#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0,1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
string s;
int arr[51];
vector<int> v;
int lens, max_num;

void dfs(int n) {
    if(n == lens) {
        for(int i = 0; i < max_num; i++) {
            cout << v[i] << " ";
        }
        exit(0);
    }

    int num;
    string tmp = "";

    for(int i = n; i <= n+1; i++) {
        tmp = tmp + s[i];
        num = stoi(tmp);

        if(num > max_num) continue;
        if(arr[num]) continue;
        v.push_back(num);
        arr[num] = 1;
        dfs(i+1);
        arr[num] = 0;
        v.pop_back();
    }
}

void solve() {
    dfs(0);
}

void input() {
    cin >> s;
    
    lens = s.length();
    
    if(lens > 9) {
        max_num = 9 + (lens - 9) / 2;
    }
    else max_num = lens;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
