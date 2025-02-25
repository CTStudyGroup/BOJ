#include <iostream>
#include <string>
using namespace std;

int n,k;
string str;
long ans=0;

void input(){
	cin>>n>>k;
	cin>>str;
}

void solve(){
	for(int i=0;i<n;i++){
		if(str[i]=='P'){
			// 오른쪽 어디까지 가도 되는지
			int r;
			if(i+k>=n) r=n-1;
			else r=i+k; 
			for(int j=i-k;j<=r;j++){
				if(str[j]=='H'){
					ans++;
					str[j]='X';
					break;
				}
			}
		}
	}
	cout<<ans;
}

int main(){
	input();
	solve();
}