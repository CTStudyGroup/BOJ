#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int n,m;
long sum[51][51]={0,};
long answer=0;

void input(){
	cin>>n>>m;
	for(int i=1;i<=n;i++){
		string temp; cin>>temp;
		for(int j=1;j<=m;j++){
			sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+temp[j-1]-'0';
		}
	}
}

void func1(){
	long temp=0;
	for(int i=1;i<=n-2;i++){
		temp=sum[i][m];
		for(int j=i+1;j<=n-1;j++){
			answer=max(answer,temp*(sum[j][m]-sum[i][m])*(sum[n][m]-sum[j][m]));
		}
	}
}

void func2(){
	long temp=0;
	for(int i=1;i<=m-2;i++){
		temp=sum[n][i];
		for(int j=i+1;j<=m-1;j++){
			answer=max(answer,temp*(sum[n][j]-sum[n][i])*(sum[n][m]-sum[n][j]));
		}
	}
}

void func3(){
	long temp=0;
	for(int i=1;i<=m-1;i++){
		temp=sum[n][m]-sum[n][i];
		for(int j=1;j<=n-1;j++){
			answer=max(answer,temp*(sum[j][i])*(sum[n][i]-sum[j][i]));
		}
	}
}


void func4(){
	long temp=0;
	for(int i=1;i<=m-1;i++){
		temp=sum[n][i];
		for(int j=1;j<=n-1;j++){
			answer=max(answer,temp*(sum[n][m]-sum[n][i]-sum[j][m]+sum[j][i])*(sum[j][m]-sum[j][i]));
		}
	}
}

void func5(){
	long temp=0;
	for(int i=1;i<=n-1;i++){
		temp=sum[i][m];
		for(int j=1;j<=m-1;j++){
			answer=max(answer,temp*(sum[n][m]-sum[i][m]-sum[n][j]+sum[i][j])*(sum[n][j]-sum[i][j]));
		}
	}
}

void func6(){
	long temp=0;
	for(int i=1;i<=n-1;i++){
		temp=sum[n][m]-sum[i][m];
		for(int j=1;j<=m-1;j++){
			answer=max(answer,temp*(sum[i][m]-sum[i][j])*(sum[i][j]));
		}
	}
}

void solve(){
	// 1.
	func1();
	func2();
	func3();
	func4();
	func5();
	func6();
}

int main(){
	input();
	solve();
}