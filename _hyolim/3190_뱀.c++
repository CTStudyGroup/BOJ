#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n,k,l;
int board[101][101]={0,};
char change[10001]={0,};
int dy[4]={0,1,0,-1};
int dx[4]={1,0,-1,0}; // 오른쪽 +1, 왼쪽 -1
queue<pair<int,int>> snake; // 뱀이 있는 곳
void printB(){
	cout<<"======board======\n";
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>k;
	for(int i=0;i<k;i++){
		int y,x; cin>>y>>x;
		board[y][x]=-1;
	}
	cin>>l;
	for(int i=0;i<l;i++){
		int x;
		char c; 
		cin>>x>>c;
		change[x]=c;
	}
}

void solve(){
	snake.push({1,1});
	int tempdir=0;

	// 자기 자신 위치는 2로 표시
	board[1][1]=2;

	for(int t=0;;++t){
		int ny=snake.back().first;
		int nx=snake.back().second;
		// cout<<ny<<" "<<nx<<"\n";
		// 이동 
		// 방향 바꿀 조건이 있는가
		if(change[t]=='D'){ // 오른쪽일 경우
			tempdir=(tempdir+1+4)%4;
		}
		if(change[t]=='L'){ // 왼쪽일 경우
			tempdir=(tempdir-1+4)%4;
		}

		// 한 칸 이동
		ny+=dy[tempdir];
		nx+=dx[tempdir];
		// cout<<ny<<" "<<nx<<"\n";

		// 종료조건
		// 1. 자기 자신과 만났을 때
		if (board[ny][nx]==2)
		{
			cout<<t+1;
			return;
		}
		// 2. 벽에 부딪혔을 때
		if (ny>n||nx>n||ny<=0||nx<=0)
		{
			cout<<t+1;
			return;
		}

		// 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
		// 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
		if(board[ny][nx]!=-1){
			// 사과가 없다면 꼬리는 갱신된다.
			board[snake.front().first][snake.front().second]=0;
			snake.pop();

		}

		// 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
		board[ny][nx]=2;
		snake.push({ny,nx});
	}
}

int main(){
	input();
	solve();
}