#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int n;
char a[55][55];
const int dy[4] = { -1,0,1,0 };
const int dx[4] = { 0,1,0,-1 };
struct g {
	int y, x;
	int status; // 세로면 0 가로면 1
};

int b1y, b1x, b2y, b2x;
int e1y, e1x, e2y, e2x;
int estatus;
int solve(int cy, int cx, int cst)
{
	//가로 세로
	int d[55][55][2];
	queue<g> q;
	memset(d, -1, sizeof(d));
	q.push({ cy,cx,cst });
	d[cy][cx][cst] = 0;

	int ret = 0;

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;
		int st = q.front().status;

		q.pop();

		for (int k = 0; k < 4; ++k) {

			int ny = y + dy[k];
			int nx = x + dx[k];

			if (!(0 <= ny && ny < n && 0 <= nx && nx < n)) continue;
			if (d[ny][nx][st] != -1) continue;

			// 세로
			if (st == 0) {
				if (ny - 1 < 0 || ny + 1 >= n) continue;
				if (a[ny - 1][nx] == '1') continue;
				if (a[ny][nx] == '1') continue;
				if (a[ny + 1][nx] == '1') continue;

				d[ny][nx][st] = d[y][x][st] + 1;
				q.push({ ny,nx,st });
			}
			// 가로
			else if (st == 1) {
				if (nx - 1 < 0 || nx + 1 >= n) continue;
				if (a[ny][nx - 1] == '1') continue;
				if (a[ny][nx] == '1') continue;
				if (a[ny][nx + 1] == '1') continue;

				d[ny][nx][st] = d[y][x][st] + 1;
				q.push({ ny,nx,st });
			}
		}
		//회전이 가능한지

		if (d[y][x][1 - st] != -1) continue;
		if (st == 0) {
			if (y - 1 < 0 || y + 1 >= n || x - 1 < 0 || x + 1 >= n) continue;

			if (a[y - 1][x - 1] != '1' && a[y][x - 1] != '1' && a[y + 1][x - 1] != '1') {
				if (a[y - 1][x + 1] != '1' && a[y][x + 1] != '1' && a[y + 1][x + 1] != '1') {

					d[y][x][1 - st] = d[y][x][st] + 1;
					q.push({ y,x,1 - st });
				}
			}
		}
		else if (st == 1) {
			if (y - 1 < 0 || y + 1 >= n || x - 1 < 0 || x + 1 >= n) continue;

			if (a[y - 1][x - 1] != '1' && a[y - 1][x] != '1' && a[y - 1][x + 1] != '1')
				if (a[y + 1][x - 1] != '1' && a[y + 1][x] != '1' && a[y + 1][x + 1] != '1') {

					d[y][x][1 - st] = d[y][x][st] + 1;
					q.push({ y,x,1 - st });
				}
		}
	}
	if (d[e2y][e2x][estatus] == -1)
		return 0;
	else return d[e2y][e2x][estatus];
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	bool flg = false;
	bool flg2 = false;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			cin >> a[i][j];
			if (a[i][j] == 'B') {
				if (flg == false) {
					b1y = i;
					b1x = j;
					flg = true;
				}
				else {
					b2y = i;
					b2x = j;
					flg = false;
				}
			}
			if (a[i][j] == 'E') {
				if (flg2 == false) {
					e1y = i;
					e1x = j;
					flg2 = true;
				}
				else {
					e2y = i;
					e2x = j;
					flg2 = false;
				}
			}
		}

	if (e2x - e1x == 0) {
		estatus = 0;
	}
	else estatus = 1;

	int ans = 0;
	if (b2x - b1x == 0) {
		ans = solve(b2y, b2x, 0);
	}
	else {
		ans = solve(b2y, b2x, 1);
	}

	cout << ans << "\n";
	return 0;
}
