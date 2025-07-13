#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0,1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N;
int arr[1001];
vector<int> v;
unordered_map<int, int> um;

bool search(int target) {
    int start = 0;
    int end = v.size()-1;

    while(start <= end) {
        int mid = (start + end) / 2;

        if(v[mid] == target) {
            return true;
        }
        else if(v[mid] > target) {
            end = mid-1;
        }
        else {
            start = mid+1;
        }
    }
    return false;
}

void solve() {
    for(int i = 0; i < N; i++) {
        for(int j = i; j < N; j++) {
            v.push_back(arr[i] + arr[j]);
        }
    }

    sort(arr, arr + N);
    sort(v.begin(), v.end());

    int sz = v.size() -1;

    for(int i = N-1; i >= 0; i--) {
        for(int j = i; j >= 0; j--) {
            int stand = arr[i] - arr[j];

            if(search(stand)) {
                cout << arr[i];
                return;
            }
        }
    }
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
        um[arr[i]]++;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
