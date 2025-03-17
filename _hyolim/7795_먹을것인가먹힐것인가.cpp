#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n,m;
int a[20001];
int b[20001];
int cnt=0;

void reset(){
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	cnt=0;
}

void printAB(){
	cout<<"------------\n";
	for(int i=0;i<n;i++) cout<<a[i]<<" ";
	cout<<"\n";
	for(int i=0;i<m;i++) cout<<b[i]<<" ";
	cout<<"\n";

}

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}

	for(int j=0;j<m;j++){
		cin>>b[j];
	}
}


void solve(){
	sort(a,a+n);
	sort(b,b+m);
	int tempcnt=0;

	for(int i=0;i<n;i++){
		for(int j=tempcnt;j<m;j++){
			if(a[i]>b[j]) {
				tempcnt++;
			}
			else{
				break;
			}
		}
		cnt+=tempcnt;
	}
}

void output(){
	cout<<cnt<<"\n";
}

int main(){
	int t;
	cin>>t;
	while(t--){
		reset();
		input();
		solve();
		output();
	}
}