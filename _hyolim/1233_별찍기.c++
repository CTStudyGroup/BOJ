#include <iostream>

using namespace std;

int n;
bool board[400][400];

void drawStar(int n,int x,int y){
	int width=4*n-3;
	int height=width+2;

	for(int i=1;i<width;i++) board[x][y--]=true;
	for(int i=1;i<height;i++) board[x++][y]=true;
	for(int i=1;i<width;i++) board[x][y++]=true;
	for(int i=1;i<height-2;i++) board[x--][y]=true;

	board[x][y]=true;
	y--;
	board[x][y]=true;

	if(n==2){
		board[x][y-1]=true;
		board[x+1][y-1]=true;
		board[x+2][y-1]=true;
		return;
	}

	drawStar(n-1,x,y-1);
}

int main(){
	cin>>n;

	if(n==1){
		cout<<"*";
		return 0;
	}

	drawStar(n,0,4*n-4);

	for(int i=0;i<4*n-1;i++){
		if(i==1){
			cout<<"*\n";
			continue;
		}
		for(int j=0;j<4*n-3;j++){
			if(board[i][j]) cout<<"*";
			else cout<<" ";
		}
		cout<<"\n";
	}
}