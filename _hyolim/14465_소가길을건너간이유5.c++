#include <iostream>

using namespace std;

int n,k,b;
bool arr[100001];
int mincnt=987654321;
void input(){
	cin>>n>>k>>b;

	for(int i=0;i<b;i++){
		int temp;
		cin>>temp;
		arr[temp-1]=true;
	}
}

void solve(){
	int cnt=0;
	for(int i=0;i<k;i++){
		if(arr[i]) cnt++;
	}
	for(int i=k;i<n;i++){
		if(arr[i-k]) cnt--;
		if(arr[i]) cnt++;
		// cout<<i+1<<" "<<cnt<<"\n";
		if(mincnt>cnt) mincnt=cnt;
	}
	cout<<mincnt;
}

int main(){
	input();
	solve();
}