#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;

int r,c;
vector<string> vec;
string col[1001];

long answer=0;

void input(){
	cin>>r>>c;
	for(int i=0;i<r;i++){
		string temp;
		cin>>temp;
		for(int j=0;j<c;j++){
			col[j]+=temp[j];
		}
	}
}

void solve(){
	int icnt=1;
	set<string> s;
	long ssize=c;

	while(icnt<=c){
		s.clear();

		// col에 있는거 다 넣기
		for(int i=0;i<c;i++){
			s.insert(col[i].substr(icnt,r));
		}

		icnt++;

		if(ssize!=s.size()){
			cout<<answer;
			return;
		}

		answer++;
	}
}

int main(){
	input();
	solve();
}