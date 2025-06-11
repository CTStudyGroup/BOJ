#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e8

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, M;
unordered_map<int, int> um;
set<pair<int, int>> st;

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        um[a] = b;
        st.insert({b, a});
    }

    cin >> M;

    for(int i = 0; i < M; i++) {
        string a;
        cin >> a;

        if(a == "add") {
            int b, c;
            cin >> b >> c;
            um[b] = c;
            st.insert({c, b});
        }
        else if(a == "recommend") {
            int b;
            cin >> b;

            if(b == 1) {        // 가장 어려운 문제
                auto it = st.rbegin();

                cout << it -> second << endl;
            }
            else {              // 가장 쉬운 문제
                auto it = st.begin();

                cout << it -> second << endl;
            }
        }
        else {
            int b;
            cin >> b;
            st.erase({um[b], b});
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
