#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

// bfs 열심히 돌리면 될 것 같은데
struct point_t{
	int y;
	int x;
};

queue<point_t> q;
char board[51][51]={0,};
int visited[51][51]={0,};
int answer=0;
int direct[4][2]={{1,0},{0,1},{-1,0},{0,-1}};

int n,m;

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
		}
	}
}

void reset(){
	memset(visited,0,sizeof(visited));
	while(!q.empty()){
		q.pop();
	}
}
void printV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<visited[i][j];
		}
		cout<<"\n";
	}
}

void bfs(int y,int x){
	q.push({y,x});
	visited[y][x]=1;
	for(point_t temp=q.front();!q.empty();q.pop()){
		temp=q.front();

		point_t next;
		for(int i=0;i<4;i++){
			next.y=temp.y+direct[i][0];
			next.x=temp.x+direct[i][1];
			if(next.y<0||next.x<0||next.y>=n||next.x>=m) continue;

			if(board[next.y][next.x]=='W') continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=visited[temp.y][temp.x]+1;
			if(answer<visited[next.y][next.x]) answer=visited[next.y][next.x];
			q.push(next);
		}
	}
}



void solve(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			reset();
			if(board[i][j]=='L') bfs(i,j);
		}
	}
}

int main(){
	input();
	solve();
	cout<<answer-1;
}