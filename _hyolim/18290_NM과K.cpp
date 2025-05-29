#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int arr[10][10]={0,};
int n,m,k;
bool visited[10][10];
long answer=0;

void input(){
	cin>>n>>m>>k;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{	
			cin>>arr[i][j];
		}
	}
}

void solve(int depth,long cnt){
	if(depth==k){
		if(answer<cnt) answer=cnt;
		return;
	}

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if(visited[i][j]) continue;
			if(i!=0&&visited[i-1][j]) continue;
			if(j!=0&&visited[i][j-1]) continue;
			if(i!=n-1&&visited[i+1][j]) continue;
			if(j!=m-1&&visited[i][j+1]) continue;
			visited[i][j]=true;
			solve(depth+1,cnt+arr[i][j]);
			visited[i][j]=false;
		}
	}
}

int main(){
	input();
	solve(0,0);
	cout<<answer;
}