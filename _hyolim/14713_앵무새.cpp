#include <iostream>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

int n;
vector<queue<string>> q(101);

void input(){
	cin>>n;
	string temp;
	getline(cin,temp);
	for(int i=0;i<n+1;i++){
		getline(cin,temp);
		istringstream ss(temp);
		string sbuffer;
		while(getline(ss,sbuffer,' ')) q[i].push(sbuffer);
	}
}

void solve(){
	bool check=false;
	int qsize=q[n].size();
	for(int i=0;i<qsize;i++){
		string base=q[n].front();
		for(int j=0;j<n;j++){
			if(!q[j].empty()&&q[j].front()==base){
				q[j].pop();
				q[n].pop();
				check=true;
				break;
			}
		}
		if(!check){
			cout<<"Impossible";
			return;
		}
		check=false;
	}

	for(int i=0;i<n;i++){
		if(!q[i].empty()){
			cout<<"Impossible";
			return;
		}
	}
	cout<<"Possible";
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
}