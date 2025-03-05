#include <iostream>

using namespace std;

int arr[50];
int n;
int cnt=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

bool check(){
	for(int i=0;i<n;i++){
		if(arr[i]) return false;
	}
	return true;
}

void solve(){
	while(!check()){
		for(auto& e:arr){
			if(e%2!=0) {
				e--;
				cnt++;
			}
		}

		if(check()) break;
		for(auto& e:arr){
			e/=2;
		}
		cnt++;

	}
}

int main(){
	input();
	solve();
	cout<<cnt;
}