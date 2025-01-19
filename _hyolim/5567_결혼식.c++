#include <iostream>
#include <vector>
#include <set>
using namespace std;

// 자신의 친구와 친구의 친구를 초대
int n;
vector<int> vec[502];
set<int> s;

void input(){
	cin>>n;
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int temp1,temp2;
		cin>>temp1>>temp2;

		vec[temp1].push_back(temp2);
		vec[temp2].push_back(temp1);
	}
}

void solve(){
	for(int i=0;i<vec[1].size();i++){
		// 바로 친구 넣기
		s.insert(vec[1][i]);

		// 친구의 친구 넣기
		for(int j=0;j<vec[vec[1][i]].size();j++){
			s.insert(vec[vec[1][i]][j]);
		}
	}

	if(s.find(1)!=s.end()) s.erase(1);
	cout<<s.size();
}

int main(){
	input();
	solve();
}