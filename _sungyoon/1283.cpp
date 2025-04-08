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
vector<string> v;
int arr[31];
map<int, int> m;
vector<vector<int>> res(31);

void solve() {
    memset(arr, -1, sizeof(arr));

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < v[i].length(); j++) {
            if(j == 0) {
                res[i].push_back(j);
            }
            else if(v[i][j] == ' ') {
                res[i].push_back(j+1);
            }
        }
    }

    for(int i = 0; i < N; i++) {
        bool visited = false;
        for(auto &it : res[i]) {
            int stand = v[i][it];
            if(m.find(stand) != m.end()) {
                continue;
            }
            else {
                if(stand > 91) {
                    m[stand] = 1;
                    m[stand-32] = 1;
                    visited = true;
                    arr[i] = it;
                    break;
                }
                else {
                    m[stand] = 1;
                    m[stand+32] = 1;
                    visited = true;
                    arr[i] = it;
                    break;
                }
            }
        }
        if(!visited) {
            for(int j = 1; j < v[i].size(); j++) {
                int stand = v[i][j];
                if(stand == 32) continue;
                if(m.find(stand) != m.end()) {
                    continue;
                }
                else {
                    if(stand > 91) {
                        m[stand] = 1;
                        m[stand-32] = 1;
                        arr[i] = j;
                        break;
                    }
                    else {
                        m[stand] = 1;
                        m[stand-32] = 1;
                        arr[i] = j;
                        break;
                    }
                }
            }
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < v[i].size(); j++) {
            if(arr[i] == j) {
                cout << '[' << v[i][j] << ']';
                continue;
            }
            cout << v[i][j];
        }
        cout << endl;
    }
}

void input() {
    cin >> N;

    cin.ignore();

    for(int i = 0; i < N; i++) {
        string s;
        getline(cin, s);
        v.push_back(s);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
