#include <iostream>
#include <string>

using namespace std;

string w;
int k;
int n;
int minans=987654321;
int maxans=0;

void reset(){
	minans=987654321;
	maxans=0;
}

void input(){
	cin>>w>>k;
	n=w.length();
}

void solve(){
	// 둘 다 투포인터로 확인하는데  
	for(int i=0;i<n;i++){
		// i 랑 확인하는거
		int cnt=0;

		for(int j=i;j<n;j++){
			// cout<<"i: "<<i<<w[i]<<" j: "<<j<<w[j]<<" cnt "<<cnt<<"\n";
			if(w[i]==w[j]) cnt++;
			if(cnt==k){
				// min max 갱신
				// cout<<i<<" "<<j<<" "<<minans<<" "<<maxans<<"\n";
				if(minans>j-i+1) minans=j-i+1;
				if(maxans<j-i+1) maxans=j-i+1;
				break;
			}
		}
	}
}

void output(){
	if(minans==987654321){
		cout<<-1;
		return;
	}
	cout<<minans<<" "<<maxans;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t; cin>>t;
	for(int i=0;i<t;i++){
		reset();
		input();
		solve();
		output();
		cout<<"\n";
	}
}	