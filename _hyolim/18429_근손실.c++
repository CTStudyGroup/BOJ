#include <iostream>
#include <vector>
using namespace std;

int n,k;
int arr[10]={0,};
long answer=0;

void input(){
	cin>>n>>k;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

void rec(int depth,vector<bool> visited,int muscle){
	if(depth==n){
		answer++;
		return;
	}
	for(int i=0;i<n;i++){
		if(visited[i]) continue;
		// 조건
		if(muscle-k+arr[i]>=500){
			visited[i]=true;
			rec(depth+1,visited,muscle-k+arr[i]);
			visited[i]=false;
		}
	}
}

void solve(){
	vector<bool> visited;
	for(int i=0;i<n;i++) visited.push_back(false);


	rec(0,visited,500);

}

int main(){
	input();
	solve();
	cout<<answer;
}