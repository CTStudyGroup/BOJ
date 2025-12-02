#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    int a = 0, b = 0; // a*x + b
    bool hasX = false;

    // +, - 기준으로 분리
    vector<string> terms;
    string cur;

    // 문자열을 '+', '-' 기호 포함하여 잘라내기
    for (int i = 0; i < (int)s.size(); i++) {
        if (s[i] == '+' || s[i] == '-') {
            if (!cur.empty()) terms.push_back(cur);
            cur = "";
        }
        cur.push_back(s[i]);
    }
    if (!cur.empty()) terms.push_back(cur);

    // 각 항 파싱
    for (auto& t : terms) {
        if (t.find('x') != string::npos) {
            // x 항
            hasX = true;
            int coef = 0;

            // 계수 부분 추출
            string num = t.substr(0, t.find('x'));
            if (num == "" || num == "+") coef = 1;
            else if (num == "-") coef = 1;
            else coef = stoi(num);

            a = coef;
        }
        else {
            // 상수항
            b = stoi(t);
        }
    }

    // 적분 결과 구성
    vector<string> out;

    // ax -> (a/2)x^2 = (a/2) xx
    if (a != 0) {
        int na = a / 2;

        if (na == 1) out.push_back("xx");
        else if (na == -1) out.push_back("-xx");
        else out.push_back(to_string(na) + "xx");
    }

    // b -> b x
    if (b != 0) {
        string term;
        if (b == 1) term = "x";
        else if (b == -1) term = "-x";
        else term = to_string(b) + "x";

        out.push_back(term);
    }

    // 마지막에 적분 상수 W
    out.push_back("W");

    // 출력: +, - 기준으로 자연스럽게 연결
    string ans = out[0];
    for (int i = 1; i < (int)out.size(); i++) {
        if (out[i][0] == '-') ans += out[i];
        else ans += "+" + out[i];
    }

    cout << ans;
    return 0;
}
