#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n,k;
vector<vector<int>> vec[12];

void input(){
	cin>>n>>k;
}

void solve(){
	vec[1].push_back({1});
	vec[2].push_back({1,1});
	vec[2].push_back({2});
	vec[3].push_back({1,1,1});
	vec[3].push_back({1,2});
	vec[3].push_back({2,1});
	vec[3].push_back({3});

	// n까지
	for(int i=4;i<=n;i++){
		vector<int> temp;
		// 1추가
		for(auto e:vec[i-1]){
			e.push_back(1);
			vec[i].push_back(e);
		}
		// 2추가
		for(auto e:vec[i-2]){
			e.push_back(2);
			vec[i].push_back(e);
		}
		// 3추가
		for(auto e:vec[i-3]){
			e.push_back(3);
			vec[i].push_back(e);
		}
	}

	// 정렬
	sort(vec[n].begin(),vec[n].end());


}

void output(){
	// 안되는 경우의 수
	if(k>vec[n].size()){
		cout<<-1;
		return;
	}


	for(int i=0;i<vec[n][k-1].size()-1;i++){
		cout<<vec[n][k-1][i]<<"+";
	}
	cout<<vec[n][k-1][vec[n][k-1].size()-1];
}

int main(){
	input();
	solve();
	output();
}