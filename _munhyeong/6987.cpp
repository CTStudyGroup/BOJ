#include <iostream>
#include <vector>

using namespace std;

struct Info {
    int win;
    int draw;
    int lose;
};

bool recursive(vector<Info> &infos, int src, int dst) {
    if (src == 6) {
        for (int i = 0; i < 6; i++) {
            if (infos[i].win)
                return false;
            if (infos[i].draw)
                return false;
            if (infos[i].lose)
                return false;
        }
        return true;
    }
    
    if (dst == 6)
        return recursive(infos, src + 1, src + 2);

    // src vs dst
    bool is_true = false;
    // 승리
    if (infos[src].win && infos[dst].lose) {
        infos[src].win--;
        infos[dst].lose--;
        is_true = recursive(infos, src, dst + 1);
        infos[src].win++;
        infos[dst].lose++;
    }
    if (is_true)
        return true;

    // 무승부
    if (infos[src].draw && infos[dst].draw) {
        infos[src].draw--;
        infos[dst].draw--;
        is_true = recursive(infos, src, dst + 1);
        infos[src].draw++;
        infos[dst].draw++;
    }
    if (is_true)
        return true;

    // 패배
    if (infos[src].lose && infos[dst].win) {
        infos[src].lose--;
        infos[dst].win--;
        is_true = recursive(infos, src, dst + 1);
        infos[src].lose++;
        infos[dst].win++;
    }
    if (is_true)
        return true;
    return false;
}

int main() {
    for (int tc = 0; tc < 4; tc++) {
        vector<Info> infos(6);
        for (int i = 0; i < 6; i++)
            cin >> infos[i].win >> infos[i].draw >> infos[i].lose;

        bool is_true = recursive(infos, 0, 1);
        cout << (is_true ? 1 : 0) << " ";
    }

    return 0;
}
