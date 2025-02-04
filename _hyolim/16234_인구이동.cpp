#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

struct city{
	int y;
	int x;
	int size;
};

struct point_t{
	int y;
	int x;
};

point_t direct[4]={{-1,0},{0,-1},{1,0},{0,1}};
queue<city> q; // bfs용
vector<city> vec; // 연합 계산용
bool visited[51][51];
int board[51][51]={0,};
int n,l,r;
// bfs로 인접한거 다 찾고 & 계산, visited는 갱신 X <- 이거 반복

void input(){
	cin>>n>>l>>r;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>board[i][j];
		}
	}
}

void printB(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";

	}
}

void bfs(int y,int x){
	city temp={y,x,board[y][x]};
	vec.push_back(temp);
	visited[y][x]=1;
	for(q.push(temp);!q.empty();q.pop()){
		temp=q.front();
		city next;

		for(int i=0;i<4;i++){
			next.y=temp.y+direct[i].y;
			next.x=temp.x+direct[i].x;
			next.size=board[next.y][next.x];
			// 범위
			if(next.y<0||next.x<0||next.y>=n||next.x>=n) continue;

			// 조건
			int diff=abs(board[next.y][next.x]-board[temp.y][temp.x]);
			// cout<<diff<<l<<r<<" ";
			if(diff<l || diff>r) continue;

			// visited
			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=true;
			vec.push_back(next);
			q.push(next);

		}
	}
}

void setV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			visited[i][j]=0;
		}
	}
}

void pmove(){
	// cout<<"---------------\n";
	int psum=0;
	for(auto& e:vec){
		// cout<<e.y<<" "<<e.x<<" "<<e.size<<"\n";
		// 인구 합치기
		psum+=e.size;
	}

	psum=psum/vec.size();

	for(auto& e:vec){
		e.size=psum;
		board[e.y][e.x]=psum;
	}

	// reset
	vec.clear();
	while(!q.empty()){
		q.pop();
	}

}

void move(){
	setV();

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(visited[i][j]) continue;
			bfs(i,j);
			pmove();
		}
	}
}

bool checkr(){
	int nexty=0;
	int nextx=0;
	int tempy=0;
	int tempx=0;

	// 하나라도 l이상 r이하가 없다면 false;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			tempy=i;
			tempx=j;
			for(int i=0;i<4;i++){
				nexty=tempy+direct[i].y;
				nextx=tempx+direct[i].x;

				// 범위
				if(nexty<0||nextx<0||nexty>=n||nextx>=n) continue;

				// 조건
				int diff=abs(board[nexty][nextx]-board[tempy][tempx]);
				// cout<<"diff: "<<diff<<"\n";
				if(diff>=l&&diff<=r) {
					return true;
				}

			}
		}
	}
	return false;
}

bool check(){
	int s=board[0][0];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(board[i][j]!=s) return false;
		}
	}

	return true;
}

void solve(){
	int i=0;
	while(true){
		// 차이나는게 하나도 없으면
		if(!checkr()) break;

		// 전부 다 똑같으면
		if(check()) break;

		move();
		// printB();
		i++;
	}
	cout<<i;
}

int main(){
	input();
	// printB();
	solve();
}