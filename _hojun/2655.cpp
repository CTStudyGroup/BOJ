#include <bits/stdc++.h>

using namespace std;

struct Brick {
    int id;      // 원래 벽돌 번호
    int area;
    int height;
    int weight; 
};
bool compare(const Brick& a, const Brick& b) {
    return a.area > b.area;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    vector<Brick> bricks(n);

    for (int i = 0; i < n; i++) {
        bricks[i].id = i + 1;
        cin >> bricks[i].area >> bricks[i].height >> bricks[i].weight;
    }

    sort(bricks.begin(), bricks.end(), compare);

    vector<int> dp(n, 0);
    vector<int> trace(n, -1);

    int max_height = 0;
    int last_idx = -1;

    for (int i = 0; i < n; i++) {
        dp[i] = bricks[i].height;
        for (int j = 0; j < i; j++) {
            if (bricks[j].weight > bricks[i].weight) {
                if (dp[j] + bricks[i].height > dp[i]) {
                    dp[i] = dp[j] + bricks[i].height;
                    trace[i] = j;
                }
            }
        }
        if (dp[i] > max_height) {
            max_height = dp[i];
            last_idx = i;
        }
    }

    vector<int> result;
    int curr = last_idx;
    while (curr != -1) {
        result.push_back(bricks[curr].id);
        curr = trace[curr];
    }

    cout << result.size() << "\n";
    for (int id : result) {
        cout << id << "\n";
    }

    return 0;
}