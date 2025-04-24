#include <iostream>

using namespace std;

int map[65][65]={0,};
int n;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>map[i][j];
		}
	}
}

void solve(int y,int x){
	if(y>=n||x>=n){ // 범위 밖으로 나갈 경우
		return;
	}

	if(map[y][x]==-1){ // 승리했을 경우
		cout<<"HaruHaru";
		exit(0);
	}


	solve(y+map[y][x],x);
	solve(y,x+map[y][x]);
}
int main(){
	input();
	solve(0,0);
	cout<<"Hing";
}