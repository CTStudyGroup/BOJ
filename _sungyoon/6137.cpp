#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

const int INF = 1e9;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
char arr[2001];

void solve() {
    int lo = 0;
    int hi = N-1;

    string s = "";

    while(lo <= hi) {
        if(arr[lo] < arr[hi]) {
            s += arr[lo];
            lo++;
        }
        else if(arr[lo] > arr[hi]) {
            s += arr[hi];
            hi--;
        }
        else if(lo == hi) {
            s += arr[lo];
            lo++;
            break;
        }
        else {
            int nlo = lo+1;
            int nhi = hi-1;
            bool leftearly = false;

            while(nlo <= nhi) {
                if(arr[nlo] < arr[nhi]) {
                    leftearly = true;
                    break;
                }
                else if(arr[nlo] > arr[nhi]) {
                    leftearly = false;
                    break;
                }
                else {
                    nlo++;
                    nhi--;
                }
            }

            if(leftearly) {
                s += arr[lo];
                lo++;
            }
            else {
                s += arr[hi];
                hi--;
            }
        }
    }
    for (int i = 0; i < s.size(); i++) {
        cout << s[i];
        if ((i + 1) % 80 == 0) cout << endl;
    }
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
