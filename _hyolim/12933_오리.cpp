#include <iostream>
#include <string>
#include <vector>
using namespace std;

string str;

char c[5]={'q','u','a','c','k'};

vector<bool> visited;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin>>str;

	if(str.length()%5!=0){
		cout<<"-1";
		exit(0);
	}
	visited=vector<bool>(str.length(),false);

	int ans=0;
	int cnt=0;
	while(1){
		int targetIdx=0;
		int tempCnt=0;
		for(int i=0;i<str.length();i++){
			if(visited[i]) continue;
			if(str[i]!=c[targetIdx]) continue;
			targetIdx=(targetIdx+1)%5;
			visited[i]=true;
			tempCnt++;
		}
		// 맨 처음이 q가 아닌 경우
		if(tempCnt==0 || targetIdx!=0){
			cout<<-1;
			exit(0);
		}
		cnt+=tempCnt++;
		ans++;
		if(cnt==str.length()) break;
	}
	cout<<ans;
}