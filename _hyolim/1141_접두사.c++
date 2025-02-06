#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

// 정렬해서 접두사인 애들 지우기
string str[51];

int n;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>str[i];
	}
}

void solve(){
	sort(str,str+n);

	int temp=0;
	for(int i=1;i<n;i++){
		if(str[i].substr(0,str[temp].length())==str[temp]){
			str[temp]="";
		}
		temp=i;

	}

	// for(int i=0;i<n;i++){
	// 	cout<<str[i]<<"\n";
	// }
}

void output(){
	int ans=0;
	for(int i=0;i<n;i++){
		if(str[i]!="") ans++;
	}
	cout<<ans;
}

int main(){
	input();
	solve();
	output();
}