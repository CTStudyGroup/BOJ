#include <bits/stdc++.h>

using namespace std;

int one, two, three, four, five, six;

bool bIsEmpty() {
    return one != 0 || two != 0 || three != 0 || four != 0 || five != 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> one >> two >> three >> four >> five >> six;

    const int area = 36;
    int ans = six;

    while (bIsEmpty())
    {
        int cnt = 0;
        while (five > 0) {
            five -= 1;
            cnt = area - 25;

            one = max(one - cnt, 0);
            ans += 1;
        }
        while (four > 0) {
            four -= 1;
            cnt = area - 16;

            cnt -= min(two, 5) * 4;

            two = max(two - 5, 0);
            one = max(one - cnt, 0);
            ans += 1;
        }
        while (three > 0) {
            cnt = area - min(three, 4) * 9;

            if (three >= 4) {
                three -= 4;
                cnt = 0;
            }
            else if (three == 3) {
                three -= 3;
                cnt -= min(1, two) * 4;
                two = max(two - 1, 0);
            }
            else if (three == 2) {
                three -= 2;
                cnt -= min(3, two) * 4;
                two = max(two - 3, 0);
            }
            else if (three == 1) {
                three -= 1;
                cnt -= min(5, two) * 4;
                two = max(two - 5, 0);
            }

            one = max(one - cnt, 0);
            ans += 1;
        }
        while (two > 0) {
            cnt = area - 4 * min(two, 9);

            two = max(two - 9, 0);
            one = max(one - cnt, 0);
            ans += 1;
        }
        while (one > 0) {
            one = max(one - 36, 0);
            ans += 1;
        }

        cout << one << " " << two << " " << three << " " << four << " " << five << " " << six << endl;
    }

    cout << ans;

    return 0;
}
