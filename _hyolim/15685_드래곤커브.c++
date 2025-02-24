#include <iostream>
#include <vector>

using namespace std;

/*
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
*/

vector<int> vec;
int board[101][101]={0,};
int direct[4][2]={{0,1},{-1,0},{0,-1},{1,0}};
int r[4]={1,2,3,0};
int x,y,d,g;
//x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다.

void reset(){
	vec.clear();
}

void input(){
	cin>>x>>y>>d>>g;
	vec.push_back(d);
	board[y][x]=1;
}

void printVec(){
	for(auto e:vec){
		cout<<e<<" ";
	}
	cout<<"\n";
}

void solve(){
	// 방향 저장
	for(int i=0;i<g;i++){
		for(int j=vec.size()-1;j>=0;j--){
			// 반시계방향으로 돌리기
			vec.push_back(r[vec[j]]);
		}
		// printVec();
	}

	int tempx=x;
	int tempy=y;
	// board로 옮기기
	for(auto e:vec){
		// cout<<"*"<<tempy<<" "<<tempx<<"\n";
		// cout<<direct[e][0]<<" "<<direct[e][1]<<"\n";
		tempy+=direct[e][0];
		tempx+=direct[e][1];

		board[tempy][tempx]=1;
	}
}

void printB(){
	for(int i=0;i<10;i++){
		for(int j=0;j<10;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}
void output(){
	int answer=0;
	for(int i=0;i<100;i++){
		for(int j=0;j<100;j++){
			if(board[i][j]&&board[i+1][j]&&board[i][j+1]&&board[i+1][j+1]) answer++;
		}
	}

	cout<<answer;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	while(t--){
		reset();
		input();
		solve();
		// printB();
		// cout<<"====\n";
	}

	output();
}