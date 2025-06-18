#include <iostream>
#include <queue>
#include <string>
#include <cstring>
using namespace std;

int board[300][300]={0,}; // *=2, #=3, 
int n,m;
int x1,y11,x2,y2;
bool visited[300][300];
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};

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
	cin>>n>>m;
	cin>>x1>>y11>>x2>>y2;
	x1--; y11--; x2--; y2--;
	for(int i=0;i<n;i++){
		string temp; cin>>temp;
		for(int j=0;j<m;j++){
			if(temp[j] == '*') board[i][j] = 2;
			else if(temp[j] == '#') board[i][j] = 3;
			else board[i][j] = temp[j]-'0';
		}
	}
}

void solve(){
	int jump = 0;
	queue<pair<int,int>> q;
	q.push({x1, y11});
	visited[x1][y11] = true;

	while(1){
		queue<pair<int,int>> next;

		while(!q.empty()){
			int x = q.front().first;
			int y = q.front().second;
			q.pop();

			if(x == x2 && y == y2){
				cout << jump << "\n";
				return;
			}

			for(int d=0;d<4;d++){
				int nx = x, ny = y;
				while(1){
					nx += dx[d];
					ny += dy[d];
					if(nx<0 || ny<0 || nx>=n || ny>=m) break;
					if(board[nx][ny] == 0 || board[nx][ny] == 3){
						if(!visited[nx][ny]){
							visited[nx][ny] = true;
							q.push({nx, ny});
						}
					}
					else if(board[nx][ny] == 1){
						board[nx][ny] = 0;
						if(!visited[nx][ny]){
							visited[nx][ny] = true;
							next.push({nx, ny});
						}
						break;
					}
					else break;
				}
			}
		}

		q = next;
		jump++;
	}
}

int main(){
	input();
	solve();
}