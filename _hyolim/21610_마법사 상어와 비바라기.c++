#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct point_t{
	int y;
	int x;
};

int board[51][51]={0,};
int n,m;
int direct[8][2]={{0,-1},{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1}};
int checkd[4][2]={{-1,-1},{1,-1},{-1,1},{1,1}};

queue<pair<int, int>> ds;
vector<point_t> cloud;

void printB(){
	cout<<"--------------------\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>board[i][j];
		}
	}

	for(int i=0;i<m;i++){
		int d,s;
		cin>>d>>s;
		ds.push({d-1,s});
	}

	// 구름 생성
	cloud.push_back({n-1,0});
	cloud.push_back({n-1,1});
	cloud.push_back({n-2,0});
	cloud.push_back({n-2,1});
}

void cloudM(int d, int s){
	vector<point_t> tempCloud;

	for(auto e:cloud){
		int ny=e.y;
		int nx=e.x;

		for(int i=0;i<s;i++){
			ny+=direct[d][0];
			nx+=direct[d][1];

			// 어느 방향이든 움직일 수 있도록
			if(ny==n) ny=0;
			if(ny==-1) ny=n-1;
			if(nx==n) nx=0;
			if(nx==-1) nx=n-1;
		}

		tempCloud.push_back({ny,nx});
	}

	cloud.clear();
	cloud=tempCloud;
}

void rain(){
	for(auto e:cloud){
		board[e.y][e.x]++;
	}
}

void copyWater(){
	for(auto e:cloud){
		for(int i=0;i<4;i++){
			int ny=e.y+checkd[i][0];
			int nx=e.x+checkd[i][1];

			if(ny<0||ny>=n||nx<0||nx>=n) continue;

			if(board[ny][nx]) board[e.y][e.x]++;
		}
	}
}

		
// 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
// 이때 구름이 생기는 칸은 구름이 사라진 칸이 아니어야 한다.
void makeCloud(){
	vector<point_t> tempCloud;
	int checkC[51][51]={0,};
	for(auto e:cloud){
		checkC[e.y][e.x]=1;
	}

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(board[i][j]<2) continue;
			if(checkC[i][j]) continue;
			tempCloud.push_back({i,j});
			board[i][j]-=2;
		}
	}
	cloud.clear();
	cloud=tempCloud;
}

void solve(){
	while(!ds.empty()){
		cloudM(ds.front().first,ds.front().second);
		rain();
		// printB();
		copyWater();
		makeCloud();
		ds.pop();
	}
}

void output(){
	long ans=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			ans+=board[i][j];
		}
	}
	cout<<ans;
}

int main(){
	input();
	solve();
	output();
}              