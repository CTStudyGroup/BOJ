#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

struct team
{
    int balloons, disA, disB;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    while (true)
    {
        int N, A, B; cin >> N >> A >> B;
        if (!N && !A && !B) break;
        long long ans = 0;
        vector<team> teams(N);

        for (int i = 0; i < N; ++i) {
            cin >> teams[i].balloons >> teams[i].disA >> teams[i].disB;
        }

        // A와 B까지의 거리의 차가 큰 순서로 정렬
        sort(teams.begin(), teams.end(), [](team a, team b) { return abs(a.disA - a.disB) > abs(b.disA - b.disB); });

        for (int i = 0; i < N; ++i) {
            int Balloon = teams[i].balloons;
            int curDisA = teams[i].disA;
            int curDisB = teams[i].disB;

            if (curDisA < curDisB) {
                if (A >= Balloon) {
                    ans += Balloon * curDisA;
                    A -= Balloon;
                }
                else {
                    // A에 남은 풍선부터 전달
                    ans += curDisA * A;
                    Balloon -= A;
                    A = 0;
                    // 남은 양만큼 B에서 전달
                    ans += Balloon * curDisB;
                    B -= Balloon;
                }
            }
            else {
                if (B >= Balloon) {
                    ans += Balloon * curDisB;
                    B -= Balloon;
                }
                else {
                    ans += curDisB * B;
                    Balloon -= B;
                    B = 0;

                    ans += Balloon * curDisA;
                    A -= Balloon;
                }
            }
        }

        cout << ans;
    }
    return 0;
}