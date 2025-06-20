#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n;
bool board[51][51];
int visited[51][51];
int dy[4]={1,-1,0,0};
int dx[4]={0,0,-1,1};

void printB(){
	cout<<"----board----\n";
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		string temp; cin>>temp;
		for (int j = 0; j < n; ++j)
		{
			if(temp[j]=='1') board[i][j]=true;
		}
	}
	// printB();
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			visited[i][j]=987654321;
		}
	}
}

void solve(){
	// 1이면 통과 가능
	queue<point_t> q;
	q.push({0,0});
	point_t temp;
	visited[0][0]=0;

	for(temp=q.front();!q.empty();q.pop()){
		temp=q.front();	
		point_t next;

		for(int i=0;i<4;i++){
			next.y=dy[i]+temp.y;
			next.x=dx[i]+temp.x;

			if(next.y<0||next.x<0||next.y>=n||next.x>=n) continue;

			// 흰 문이면
			if(board[next.y][next.x]){
				if(visited[next.y][next.x]<=visited[temp.y][temp.x]) continue;
				else{
					visited[next.y][next.x]=visited[temp.y][temp.x]; //하나 부수기
					q.push(next);
				}
			}else{ // 검은 문이면
				if(visited[next.y][next.x]<=visited[temp.y][temp.x]+1) continue;
				else{
					visited[next.y][next.x]=visited[temp.y][temp.x]+1; //하나 부수기
					q.push(next);
				
				}
			}
		}
	}

	cout<<visited[n-1][n-1];
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
}