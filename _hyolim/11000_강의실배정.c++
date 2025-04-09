#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int n;
vector<pair<int, int>> classes;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int s, t;
        cin >> s >> t;
        classes.push_back({s, t});
    }

    sort(classes.begin(), classes.end());

    priority_queue<int, vector<int>, greater<int>> pq;

    for (auto [s, t] : classes) {
        if (!pq.empty() && pq.top() <= s) {
            pq.pop(); 
        }
        pq.push(t);
    }

    cout << pq.size(); 
}
