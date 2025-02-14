#include <iostream>
#include <algorithm>
#include <deque>
#include <string>
using namespace std;


deque<int> d[4];

void input(){
	string s;
	for(int i=0;i<4;i++){
		cin>>s;
		for(int j=0;j<s.length();j++){
			d[i].push_back(s[j]-'0');
		}
	}
}

void printD(){
	cout<<"-----------------\n";
	for(int i=0;i<4;i++){
		for(int j=0;j<8;j++){
			cout<<d[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void rotate(int x,int y){
	// t==true : 시계
	// t==false : 반시계
	if(y==1){
		int temp=d[x][7];
		d[x].pop_back();
		d[x].push_front(temp);
	}else{ //반시계는 앞을 빼고 뒤로 삽입
		int temp=d[x][0];
		d[x].pop_front();
		d[x].push_back(temp);
	}	
}

// x : 톱니바퀴 번호, 방향 : 1-시계, 0:반시계
void solve(int x,int y){
	// 자 먼저 x부터 오른쪽까지~
	// 돌리는거 맨 마지막에 한 번에 해야하니까 일단 체크 먼저
	x=x-1;
	int check[4]={0,};
	check[x]=y;
	

		// 이제 왼쪽 확인
	for(int i=x;i>=1;i--){
		if(d[i][6]==d[i-1][2]) break; // 같은 극이면 냅두기~
		// 다른 극이면 돌리기~
		check[i-1]=-check[i];
	}


	for(int i=x;i<3;i++){
		if(d[i][2]==d[i+1][6]) break; // 같은 극이면 냅두기~
		// 다른 극이면 돌리기~
		check[i+1]=-check[i];
	}




	for(int i=0;i<4;i++){
		if(check[i]){
			rotate(i,check[i]);
		}
	}
	// printD();
}


int output(){
	int sum=0;
	sum+=d[0][0];
	sum+=d[1][0]*2;
	sum+=d[2][0]*4;
	sum+=d[3][0]*8;

	return sum;
}

int main(){
	input();
	// printD();
	int m;
	cin>>m;
	for(int i=0;i<m;i++){
		int x,y;
		cin>>x>>y;
		solve(x,y);
	}
	cout<<output();

}