#include <iostream>
#include <queue>
#include <string>

using namespace std;

int board[1001][1001]={0,};
int fire_visited[1001][1001]={0,};
int visited[1001][1001]={0,};
int w,h;

struct point_t{
	int y;
	int x;
};

point_t direct[4]={{0,1},{1,0},{0,-1},{-1,0}};
queue<point_t> fire_q;
queue<point_t> q;

// 불 먼저 구하고, 불 visited를 조건으로 visited 구하기

void reset(){
	for(int i=0;i<1001;i++){
		for(int j=0;j<1001;j++){
			fire_visited[i][j]=0;
			visited[i][j]=0;
			board[i][j]=0;
		}
	}

	while(!q.empty()) q.pop();
	while(!fire_q.empty()) fire_q.pop();
}

void printBoard(){
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			cout<<(char)board[i][j];
		}
		cout<<"\n";
	}
	cout<<"====\n";
}

void printFvisited(){
	cout<<"=========fireVisited========\n";
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			cout<<fire_visited[i][j];
		}
		cout<<"\n";
	}
}

void printVisited(){
	cout<<"=========Visited========\n";
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			cout<<visited[i][j];
		}
		cout<<"\n";
	}
}

void input(){
	cin>>w>>h;
	for(int i=0;i<h;i++){
		string s;
		cin>>s;
		for(int j=0;j<w;j++){
			board[i][j]=s[j];	
			if(board[i][j]=='@'){
				point_t temp={i,j};
				q.push(temp);
				visited[i][j]=1;
			}	

			if(board[i][j]=='*'){
				point_t temp={i,j};
				fire_q.push(temp);
				fire_visited[i][j]=1;
			}
		}
	}
}

void fire_bfs(){
	while(!fire_q.empty()){
		point_t temp=fire_q.front();
		point_t next;
		for(int i=0;i<4;i++){
			next.y=temp.y+direct[i].y;
			next.x=temp.x+direct[i].x;

			// 범위
			if(next.y<0||next.x<0||next.y>=h||next.x>=w) continue;

			// 조건
			if(board[next.y][next.x]=='#') continue;

			if(fire_visited[next.y][next.x]) continue;

			fire_visited[next.y][next.x]=fire_visited[temp.y][temp.x]+1;
			fire_q.push(next);
		}

		fire_q.pop();
	}

	// printFvisited();
}

void bfs(){

	while(!q.empty()){
		point_t temp=q.front();
		point_t next;
		for(int i=0;i<4;i++){
			next.y=temp.y+direct[i].y;
			next.x=temp.x+direct[i].x;

			// 범위
			if(next.y<0||next.x<0||next.y>=h||next.x>=w) continue;

			// 조건 1. 벽이 아닐 것
			if(board[next.y][next.x]=='#') continue;

			// 조건 2. 불 보다 앞서야할 것
			if(visited[temp.y][temp.x]+1>=fire_visited[next.y][next.x] && fire_visited[next.y][next.x]) continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=visited[temp.y][temp.x]+1;
			q.push(next);
		}

		q.pop();
	}

	// printVisited();
}

void solve(){
	fire_bfs();
	bfs();
}

void output(){
	//외곽 돌면서 가장 작은 수 찾기
	int ans=21e8;
	for(int i=0;i<w;i++){
		if(ans>visited[0][i]&&visited[0][i]) ans=visited[0][i];
		if(ans>visited[h-1][i]&&visited[h-1][i]) ans=visited[h-1][i];	
	}

	for(int i=0;i<h;i++){
		if(ans>visited[i][0]&&visited[i][0]) ans=visited[i][0];
		if(ans>visited[i][w-1]&&visited[i][w-1]) ans=visited[i][w-1];	
	}

	if(ans==21e8) cout<<"IMPOSSIBLE\n";
	else cout<<ans<<"\n";
}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		reset();
		input();
		solve();
		output();
	}
}