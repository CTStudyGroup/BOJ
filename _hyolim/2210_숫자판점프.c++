#include <iostream>
#include <set>
#include <vector>
using namespace std;


int dy[4]={-1,1,0,0};
int dx[4]={0,0,1,-1};

int board[5][5];
set<vector<int>> s;

void input(){
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			cin>>board[i][j];
		}
	}
}

void rec(int depth,vector<int> temp,int y,int x){
	if(depth==6){
		s.insert(temp);
		return;
	}

	int ny,nx;
	for(int i=0;i<4;i++){
		ny=y+dy[i];
		nx=x+dx[i];

		if(ny<0||nx<0||ny>=5||nx>=5) continue;

		temp.push_back(board[ny][nx]);
		rec(depth+1,temp,ny,nx);
		temp.pop_back();

	}
}

void solve(){
	vector<int> temp;
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			rec(0,temp,i,j);
		}
	}
	cout<<s.size();
}

int main(){
	input();
	solve();
}