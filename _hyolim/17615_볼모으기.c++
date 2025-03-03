#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n,sw,cnt,m=500001;
char arr[500001];

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}

}

void set(){
	sw=0;
	m=cnt<m?cnt:m;
	cnt=0;
}

void solve(){
	// 빨간색을 왼쪽으로 모을 경우
	for(int i=0;i<n;i++){
		if(arr[i]=='B') sw=1;
		if(sw&&arr[i]=='R') cnt++;
	} set();

	// 빨간색을 오른쪽으로 모을 경우
	for(int i=n-1;i>=0;i--){
		if(arr[i]=='B') sw=1;
		if(sw&&arr[i]=='R') cnt++;
	} set();

	// 파란색을 왼쪽으로 모을 경우
	for(int i=0;i<n;i++){
		if(arr[i]=='R') sw=1;
		if(sw&&arr[i]=='B') cnt++;
	} set();

	// 파란색을 오른쪽으로 모을 경우
	for(int i=n-1;i>=0;i--){
		if(arr[i]=='R') sw=1;
		if(sw&&arr[i]=='B') cnt++;
	} set();

	cout<<m;
}

int main(){
	input();
	solve();

}