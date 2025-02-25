#include <iostream>

using namespace std;

int h,w;
int arr[501];
int board[501][501]={0,};
long ans=0;

void input(){	
	cin>>h>>w;
	for(int i=0;i<w;i++){
		cin>>arr[i];
	}

	for(int i=0;i<w;i++){
		for(int j=0;j<arr[i];j++){
			board[h-1-j][i]=1;
		}
	}
}

void solve(){
	int st=-1;
	for(int i=h-1;i>=0;i--){
		st=-1;
		for(int j=0;j<w;j++){
			if(board[i][j]){
				if(st!=-1) ans+=j-st-1;
				st=j;
			}
		}
	}
	cout<<ans;
}

int main(){
	input();
	solve();
}