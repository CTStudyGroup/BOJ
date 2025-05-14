#include <iostream>
#include <string>
using namespace std;

int n,m;
int a[51][51]={0,};
int b[51][51]={0,};

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		string temp; cin>>temp;
		for(int j=0;j<m;j++){

			a[i][j]=temp[j]-'0';
		}
	}

	for(int i=0;i<n;i++){
		string temp; cin>>temp;

		for(int j=0;j<m;j++){
			b[i][j]=temp[j]-'0';
		}
	}

}

void printA(){
	cout<<"---A---\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<a[i][j]<<" ";
		}
		cout<<"\n";
	}
}

bool check(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(a[i][j]!=b[i][j]) return false;
		}
	}
	return true;
}

void turn(int y,int x){
	for(int i=y;i<y+3;i++){
		for(int j=x;j<x+3;j++){
			if(a[i][j]) a[i][j]=0;
			else a[i][j]=1;
		}
	}
}

void solve(){
	long answer=0;
	// 다르면 바로바로 뒤집기
	for(int i=0;i<n-2;i++){
		for(int j=0;j<m-2;j++){
			if(check()){
				cout<<answer;
				return;
			}

			if(a[i][j]!=b[i][j]){
				turn(i,j);
				answer++;
			}
			// printA();
		}
	}
	if(check()){
		cout<<answer;
		return;
	}
	cout<<-1;
}

int main(){
	input();
	solve();
}