#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int n,m;
int arr[10000];
set<vector<int>> s;

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	sort(arr,arr+n);

}

void solve(int depth,vector<int> vec){
	if(depth==m){
		s.insert(vec);
		return;
	}
	for(int i=0;i<n;i++){
		vec.push_back(arr[i]);
		solve(depth+1,vec);
		vec.pop_back();
	}
}

void output(){
	for(auto e:s){
		for(auto f:e){
			cout<<f<<" ";
		}
		cout<<"\n";
	}
}
int main(){
	input();
	vector<int> v;
	solve(0,v);
	output();
}