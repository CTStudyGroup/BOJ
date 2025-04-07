#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n,k;
int arr[10001];
vector<int> vec;

long answer=0;

void input(){
	cin>>n>>k;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

void solve(){
	sort(arr,arr+n);

	for(int i=0;i<n-1;i++){
		vec.push_back(arr[i+1]-arr[i]);
	}

	sort(vec.begin(),vec.end(),greater<int>());
	k--;
	while(k--){
		if(vec.empty()) break;
		vec.erase(vec.begin());
	}
	
	for(auto e:vec){
		answer+=e;
	}
	cout<<answer;
}

int main(){
	input();
	solve();
}