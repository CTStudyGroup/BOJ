#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n;

    //음식 이름 배열
    vector<vector<string>> foods(n);

    for (int i = 0; i < n; ++i) {
        //현재 나온 
        vector<string> curStr;

        cin >> m;
        while (m--) {
            string str;
            cin >> str;
            curStr.push_back(str);
        }
        foods[i] = curStr;
    }

    sort(foods.begin(), foods.end());

    //위에 나오는 먹이와 겹치지 않는 인덱스를 찾기
    for (int i = 0; i < n; i++) {
        int diff = 0;
        if (i != 0) {
            for (int j = 0;j < foods[i].size() && j < foods[i - 1].size();j++) {
                if (foods[i][j] == foods[i - 1][j]) diff++;
                else break;
            }
        }
        for (int j = diff;j < foods[i].size();j++) {
            string ret;
            int k = j;

            while (k--) ret += "--";
            cout << ret + foods[i][j] << '\n';
        }
    }


    return 0;
}
