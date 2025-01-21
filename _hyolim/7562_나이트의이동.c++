#include <iostream>
#include <queue>

using namespace std;

struct point_t{
	int y;
	int x;
};

int direct[8][2]={{-1,-2},{-2,-1},{1,2},{2,1},{1,-2},{-1,2},{-2,1},{2,-1}};
int t;	// 테케 개수
queue<point_t> q;
int n; 	// 체스판 길이
int visited[301][301]={0,};
int curY,curX;
int dY,dX;

void reset(){
	for(int i=0;i<301;i++){
		for(int j=0;j<301;j++){
			visited[i][j]=0;
		}
	}
	while(!q.empty()){
		q.pop();
	}
}

void input(){
	cin>>n;
	cin>>curY>>curX;
	cin>>dY>>dX;
}

void solve(){
	point_t cur={curY,curX};
	visited[curY][curX]=1;

	for(q.push(cur);!q.empty();q.pop()){
		// 하나 꺼내오고
		point_t temp=q.front();
		point_t nxt;

		// 다음꺼 계산
		for(int i=0;i<8;i++){
			nxt.y=temp.y+direct[i][0];
			nxt.x=temp.x+direct[i][1];

			// 범위 계산
			if(nxt.y<0||nxt.y>=n||nxt.x<0||nxt.x>=n) continue;

			// visited 조건
			if(visited[nxt.y][nxt.x]) continue;

			// visited 계산
			visited[nxt.y][nxt.x]=visited[temp.y][temp.x]+1;
			q.push(nxt);

			if(nxt.y==dY && nxt.x==dX){
				return;
			}
		
		}
	}
}

void output(){
	cout<<visited[dY][dX]-1<<"\n";
}

int main(){
	cin>>t;
	for(int i=0;i<t;i++){
		reset();
		input();
		solve();
		output();
	}
}	