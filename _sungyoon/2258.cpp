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

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int N, M;
vector<pii> v;

bool compare(pii a, pii b) {
    if(a.second == b.second) {
        return a.first > b.first;
    }

    return a.second < b.second;
}

void Print() {
    for(auto it : v) {
        cout << it.first << " " << it.second << endl;
    }
}

void solve() {
    sort(v.begin(), v.end(), compare);

    int sum_weight = 0;
    int sum_price = 0;
    int before = -1;
    for (int i = 0; i < v.size(); i++)
    {
        if (sum_weight < M)
        {
            // 가격이 같을 경우
            if (before == v[i].second)
            {
                sum_price += v[i].second;
            }
            else
            {
                before = sum_price = v[i].second;
            }
        }
        else
        {
            //같은 가격 여러개 vs 비싼놈 하나 비교 필요
            if ((before != v[i].second) && (sum_price >= v[i].second))
            {
                before = sum_price = v[i].second;
            }
        }

        sum_weight += v[i].first;
    }

    if(sum_weight < M) {
        cout << -1;
    }
    else {
        cout << sum_price;
    }
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

