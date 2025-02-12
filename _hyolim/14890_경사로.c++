#include <iostream>
#include <cmath>
using namespace std;

// 행, 열을 각각 돌면서 차이나는 곳이 발생했을 때, 방향과 위치를 알려줘서 경사로를 만들 수 있는 것인지
// 확인하는 함수 추가. 가능하면 계속 탐색
// 그렇게 행, 열을 각각 돌기
// 0:위 1:아래 2:오른쪽 3:왼쪽
int n,l;
int board[101][101]={0,};
int d[4][2]={{-1,0},{1,0},{0,1},{0,-1}};
int answer=0;
bool visited[101][101];

void printB(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>l;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>board[i][j];
		}
	}
	// printB();
}

void clearV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			visited[i][j]=false;
		}
	}
}

bool check(int y,int x,int di){
	// 위일 경우
	if(di==0&&y-l+1<0) return false;
	// 아래
	if(di==1&&y+l-1>=n) return false;
	// 오른쪽
	if(di==2&&x+l-1>=n) return false;
	// 왼쪽 
	if(di==3&&x-l+1<0) return false;

	int ny=y,nx=x;
	if(visited[ny][nx]) return false;
	// cout<<"-----검증----\n";
	// 각 방향으로 같은 숫자가 있는지 확인
	for(int i=1;i<l;i++){
		ny+=d[di][0];
		nx+=d[di][1];
		// cout<<board[ny][nx]<<" "<<board[y][x]<<"\n";
		if(visited[ny][nx]) return false;
		// cout<<"&";
		if(board[y][x]!=board[ny][nx]) return false;
	}
	return true;
}

void setV(int y,int x,int di){
	int ny=y,nx=x;
	visited[ny][nx]=true;
	// 각 방향으로 같은 숫자가 있는지 확인
	for(int i=1;i<l;i++){
		ny+=d[di][0];
		nx+=d[di][1];
		visited[ny][nx]=true;
	}
}

void solve(){
	// 행 먼저 가능한거 확인
	for(int i=0;i<n;i++){
		bool sig=true;
		int tempn=board[i][0];
		for(int j=1;j<n;j++){
			if(tempn==board[i][j]) continue;
			// 만약 다르면 경사로 놓을 수 있는지 확인
			// 먼저 차이가 2이상 나면 안됨
			if(abs(tempn-board[i][j])>=2) {
				sig=false;
				break;
			}
			// cout<<"TEMPN : "<<tempn<<" "<<board[i][j]<<"\n";
			if(tempn>board[i][j]){ // 왼쪽이 더 큰 경우
				if(check(i,j,2)){ // 오른쪽으로 놓을 수 있는지 확인
					tempn=board[i][j];
					setV(i,j,2);
				}else{
					sig=false;
					break; // 이 행은 글렀음
				}
			}
			if(tempn<board[i][j]){ // 오른쪽이 더 큰 경우
				if(check(i,j-1,3)){
					tempn=board[i][j];
					setV(i,j-1,3);
				}else{
					sig=false;
					break;
				}
			}
		}
		// cout<<"result : "<<sig<<"\n\n";
		if(sig) answer++;
	}

	clearV();
	// 열 가능한거 확인
	for(int j=0;j<n;j++){
		bool sig=true;
		int tempn=board[0][j];
		for(int i=1;i<n;i++){
			if(tempn==board[i][j]) continue;
			// 만약 다르면 경사로 놓을 수 있는지 확인
			// 먼저 차이가 2이상 나면 안됨
			if(abs(tempn-board[i][j])>=2) {
				sig=false;
				break;
			}
			// cout<<"TEMPN : "<<tempn<<" "<<board[i][j]<<"\n";
			if(tempn>board[i][j]){ // 아래가 더 작은 경우
				if(check(i,j,1)){ 
					// cout<<"*";
					tempn=board[i][j];
					setV(i,j,1);
				}else{
					sig=false;
					break; // 이 행은 글렀음
				}
			}
			if(tempn<board[i][j]){ // 위가 더 큰 경우
				if(check(i-1,j,0)){
					tempn=board[i][j];
					setV(i-1,j,0);
				}else{
					sig=false;
					break;
				}
			}
		}
		// cout<<j<<"result : "<<sig<<"\n\n";
		if(sig) answer++;
	}

}

int main(){
	input();
	solve();
	cout<<answer;
}