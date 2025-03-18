#include <iostream>
#include <vector>

using namespace std;

int n,k;
vector<int> vec[152];
bool visited[152];

void input(){
	cin>>n>>k;
	for(int i=0;i<n;i++){
		int temp;
		cin>>temp;
		vec[i].push_back(temp);
	}

}

void solve(int depth,int idx){
	if(idx==k){
		cout<<depth;
		exit(0);
	}

	if(visited[vec[idx][0]]) return;
	visited[vec[idx][0]]=true;
	solve(depth+1,vec[idx][0]);


}

int main(){
	input();
	solve(0,0);
	cout<<"-1";
}