#include <iostream>
#include <queue>
using namespace std;

/*
1. 구멍 밖 한 군데를 찾아서 bfs 돌면서 vistied 채우기;
2. 구멍과 맞닿아있으면 지우기 -> tempboard 사용
3. 반복
*/

struct point_t{
	int y;
	int x;
};

int n,m;
int direct[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
int board[101][101]={0,};
bool visited[101][101];

void printB(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void printV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<visited[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void resetV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			visited[i][j]=false;
		}
	}
}

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
		}
	}
}

void bfs(){
	point_t temp={0,0};
	queue<point_t> q;
	q.push(temp);
	visited[0][0]=true;
	for(temp=q.front();!q.empty();q.pop()){
		temp=q.front();
		point_t next;
		for(int i=0;i<4;i++){
			next.y=temp.y+direct[i][0];
			next.x=temp.x+direct[i][1];
			
			if(next.y<0||next.x<0||next.y>=n||next.x>=m) continue;

			if(board[next.y][next.x]) continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=true;
			q.push(next);
		}
	}
	// printV();
}

bool check(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(board[i][j]) return true;
		}
	}
	return false;
}

int left(){
	int cnt=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(board[i][j]) cnt++;
		}
	}
	return cnt;
}
void remove(){
	int tempB[101][101]={0,};
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			for(int k=0;k<4;k++){
				int y=i+direct[k][0];
				int x=j+direct[k][1];

				if(visited[y][x]){
					tempB[i][j]=1;
				}
			}
		}
	}

	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(tempB[i][j]) board[i][j]=0;
		}
	}

}

void solve(){
	int answer=0;
	int cnt=0;
	while(check()){
		cnt=left();

		resetV();
		bfs();
		remove();
		answer++;
	}	
	cout<<answer<<"\n"<<cnt;
}


int main(){
	input();
	solve();
}