#include <iostream>
#include <string>
#include <cstring>

using namespace std;

string s1,s2,s3;
int visited[201][201];

void dfs(int idx1,int idx2){
	if(visited[idx1][idx2]) return;
	visited[idx1][idx2]=1;

	if(s1[idx1]==s3[idx1+idx2]) dfs(idx1+1,idx2);
	if(s2[idx2]==s3[idx1+idx2]) dfs(idx1,idx2+1);
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

	int t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		memset(visited,0,sizeof(visited));
		cin>>s1>>s2>>s3;
		int s1len=s1.length(), s2len=s2.length();
		s1+='*',s2+='*',s3+='#';
		dfs(0,0);

		cout<<"Data set "<<i+1<<": ";
		if(visited[s1len][s2len]) cout<<"yes\n";
		else cout<<"no\n";
	}
}