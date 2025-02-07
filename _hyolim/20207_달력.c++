#include <iostream>
#include <algorithm>
using namespace std;

// 정렬 후에 반복문 돌면서 ++하기
// 0이 나오는 순간까지의 거리와 그때 가장 큰 빈도를 구해서 곱하면 됨
// 1base 

int board[367]={0,};
int n;
long ans=0;

void printB(){
	for(int i=1;i<=365;i++){
		cout<<board[i]<<" ";
	}
}

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int st,fi;
		cin>>st>>fi;
		for(int j=st;j<=fi;j++){
			board[j]++;
		}
	}

	// printB();

}

void solve(){
	int maxx=-1;
	int maxy=0;
	int i=1;
	while(i<=366){
		if(!board[i]){
			// cout<<"*"<<maxx<<" "<<maxy<<"\n";
			ans+=maxx*maxy;
			maxx=-1;
			maxy=0;
			i++;
			continue;
		}

		maxx=max(board[i],maxx);
		maxy++;
		// cout<<maxx<<" "<<maxy<<"\n ";
		i++;
	}
}

int main(){
	input();
	solve();
	cout<<ans;
}