#include <iostream>
#include <vector>
int N;

using namespace std;
vector<vector<int> > board;

//4방향
int dy[] = { 0,1,0,-1 };
int dx[] = { -1, 0,1,0 };

// 움직이는 모래의 정도
double p[9] = { 0.05, 0.1, 0.1, 0.02, 0.02, 0.07, 0.07, 0.01, 0.01 };

int m_dy[4][10] = {
	{0,-1,1, -2,2,-1,1,-1,1,0},
	{2,1,1,0,0,0,0,-1,-1,1},
	{0,-1,1, -2,2,-1,1,-1,1,0},
	{-2,-1,-1,0,0,0,0,1,1,-1}
};
int m_dx[4][10] = {
	{-2,-1,-1,0,0,0,0,1,1,-1},
	{0,-1,1, -2,2,-1,1,-1,1,0},
	{2,1,1,0,0,0,0,-1,-1,1},
	{0,-1,1, -2,2,-1,1,-1,1,0}
};
int result = 0;
int cnt = 0;

void check() {
	int y = N / 2, x = N / 2; // 배열의 중간 좌표
	int a;
	int dist = 1;
	int d = 0; 
	int cnt = 0; // 두 번 이동 확인용 count 변수
	while (1) {
		cnt++;

		//dist만큼 d방향으로 이동
		for (int m = 0; m < dist; m++) { 
			int ny = y + dy[d];  // d 방향으로 이동
			int nx = x + dx[d];  // d 방향으로 이동
			y = ny;
			x = nx;
			a = board[ny][nx]; // 이동한 모래 
			for (int k = 0; k < 9; k++) {
				int m_ny = ny + m_dy[d][k]; //흩날리는 모래 y 좌표
				int m_nx = nx + m_dx[d][k]; //흩날리는 모래 x 좌표

				int sand = (int)(board[ny][nx] * p[k]); //흩날리는 모래 양
				a -= sand; // 이동한 모래에서 흩날리는 모래를 빼줌
				if (m_ny < 0 || m_ny >= N || m_nx < 0 || m_nx >= N)  // 격자 밖으로 이동한 경우 result에 흩날린 모래를 추가
					result += sand; 
				else   // 격자 안인 경우 해당 좌표에 흩날리는 모래 양 추가
					board[m_ny][m_nx] += sand; 
				
			}
			//나머지 모래 이동
			int m_ny = ny + m_dy[d][9]; 
			int m_nx = nx + m_dx[d][9];
			if (m_ny < 0 || m_ny >= N || m_nx < 0 || m_nx >= N) {
				result += a;
			}
			else
				board[m_ny][m_nx] += a;

			board[ny][nx] = 0; // 이동 후 모래 = 0으로 지정
			if (ny == 0 && nx == 0) //이동 후 좌표가 (0, 0)인 경우 종료
				return;
		}
		if (cnt == 2) {  
			//두 번 이동한 경우 dist+=1
			dist++;
			cnt = 0;
		}
		d = (d + 1) % 4; // 이동 방향을 바꿈
	}
}

int main()
{
	cin >> N;
	board = vector<vector<int> >(N, vector<int>(N, 0));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}
	check();
	cout << result;
}
