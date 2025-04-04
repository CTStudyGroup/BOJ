#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n,m,k;
int board[20][20]={0,};
int dice[6]={2,4,1,3,5,6};
int dy[4]={0,0,1,-1}; // 동서남북
int dx[4]={1,-1,0,0};
int tempD=0;
int clockD[4]={2,3,1,0}; // 시계 방향용
int reclockD[4]={3,2,0,1}; // 반시계방향용
int reverD[4]={1,0,3,2}; // 반대로 갈 경우 방향용
long answer=0;

void printB(){
	cout<<"---board---\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}
void input(){
	cin>>n>>m>>k;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
		}
	}
	// printB();
}

void printDice(){
	cout<<"---dice---\n";
	for(int i=0;i<6;i++){
		cout<<dice[i]<<" ";
	}
	cout<<"\n";
}

void rollDice(int d){ // 이동방향
	if(d==0){ // 동
		int temp=dice[5];
		dice[5]=dice[3];
		dice[3]=dice[2];
		dice[2]=dice[1];
		dice[1]=temp;
		return;
	}
	if(d==1){ // 서
		int temp=dice[1];
		dice[1]=dice[2];
		dice[2]=dice[3];
		dice[3]=dice[5];
		dice[5]=temp;
		return;

	}
	if(d==2){ // 남

		int temp=dice[5];
		dice[5]=dice[4];
		dice[4]=dice[2];
		dice[2]=dice[0];
		dice[0]=temp;
		return;
	}
	if(d==3){ // 북
		int temp=dice[0];
		dice[0]=dice[2];
		dice[2]=dice[4];
		dice[4]=dice[5];
		dice[5]=temp;
		return;
	}
}

int getScore(point_t temp,int num){
	queue<point_t> q;
	q.push(temp);
	bool visited[20][20];
	memset(visited,false,sizeof(visited));
	visited[temp.y][temp.x]=true;
	int cnt=1;

	for(;!q.empty();q.pop()){
		temp=q.front();
		point_t next;
		for(int i=0;i<4;i++){
			next.y=temp.y+dy[i];
			next.x=temp.x+dx[i];

			if(next.y<0||next.x<0||next.y>=n||next.x>=m) continue;

			if(visited[next.y][next.x]) continue;

			if(board[next.y][next.x]!=num) continue;

			visited[next.y][next.x]=true;
			cnt++;
			q.push(next); 
		}

	}
	// cout<<cnt<<" "<<num<<" ,";
	return cnt*num;
}

void solve(){
	// 주사위 바닥면은 dice[5]
	int y=0;
	int x=0;

	while(k--){
		// 1.주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
		// 다음에 갈 곳
		int ny=dy[tempD]+y;
		int nx=dx[tempD]+x;

		// 못간다면?
		if(ny<0||nx<0||ny>=n||nx>=m){
			tempD=reverD[tempD];
			// 뒤집기
			ny=dy[tempD]+y;
			nx=dx[tempD]+x;
		}
		// printDice();
		// cout<<"\n"<<tempD<<"\n";
		rollDice(tempD);
		// printDice();
		// 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
		answer+=getScore({ny,nx},board[ny][nx]);
		// cout<<answer<<"\n";

		// 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
		if(board[ny][nx]<dice[5]){ // A>B 이동방향 시계방향
			tempD=clockD[tempD];
		} else if(board[ny][nx]>dice[5]){ // A<B 이동방향 반시계
			tempD=reclockD[tempD];
		} 
		

		// cout<<"n : "<<ny<<" "<<nx<<", "<<tempD<<", "<<board[ny][nx]<<" "<<dice[5]<<": ";
		// printDice();
		y=ny;
		x=nx;

	}
}

void output(){
	cout<<answer;
}

int main(){
	input();
	solve();
	output();
}