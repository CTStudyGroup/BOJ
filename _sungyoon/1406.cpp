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

struct FISH {
    int x;
    int y;
    int Dir;
    bool live;
};

//int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int M;

void input() {
    string s;
    cin >> s >> M;

    list<char> li(s.begin(), s.end());

    auto idx = li.end();

    for(int i = 0; i < M; i++) {
        char a;
        cin >> a;

        if(a == 'L') {
            if(idx != li.begin()) idx--;
        }
        else if(a == 'D') {
            if(idx != li.end()) idx++;
        }
        else if(a == 'B') {
            if(idx != li.begin()) {
                idx--;
                idx = li.erase(idx);
            }
        }
        else {
            char b;
            cin >> b;
            li.insert(idx, b);
        }
    }

    for(auto it : li) {
        cout << it;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
